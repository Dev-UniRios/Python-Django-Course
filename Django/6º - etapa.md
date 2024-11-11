# 6º To-Do List com Django

## Objetivo

Adicionar a funcionalidade de upload de imagens às tarefas utilizando o pacote `django-stdimage`, permitindo que os usuários anexem imagens às suas tarefas.

---

### Passo a passo

#### Parte 1: Instalar e configurar o `django-stdimage`

1. **Instalar o pacote `django-stdimage`**:
   - No terminal, instale o pacote usando o `pip`:
     ```bash
     pip install django-stdimage
     ```

2. **Adicionar `stdimage` ao `INSTALLED_APPS`**:
   - No arquivo `settings.py` do projeto, adicione `'stdimage'` à lista de aplicações instaladas:
     ```python
     INSTALLED_APPS = [
         # Apps Django padrão
         'django.contrib.admin',
         'django.contrib.auth',
         'django.contrib.contenttypes',
         'django.contrib.sessions',
         'django.contrib.messages',
         'django.contrib.staticfiles',
         # Apps de terceiros
         'bootstrap4',
         'stdimage',
         # App tarefas
         'tarefas',
     ]
     ```

#### Parte 2: Atualizar o modelo `Tarefa` para incluir um campo de imagem

1. **Modificar o modelo `Tarefa`**:
   - No arquivo `models.py` da aplicação `tarefas`, importe `StdImageField` e adicione um campo de imagem ao modelo `Tarefa`:
     ```python
     # tarefas/models.py

     from django.db import models
     from django.contrib.auth.models import User
     from stdimage.models import StdImageField

     class Tarefa(models.Model):
         titulo = models.CharField(max_length=100)
         concluida = models.BooleanField(default=False)
         usuario = models.ForeignKey(User, on_delete=models.CASCADE)
         imagem = StdImageField(upload_to='tarefas', variations={'thumb': (100, 100)}, blank=True, null=True)

         def __str__(self):
             return self.titulo

         class Meta:
             ordering = ['-id']
     ```

2. **Aplicar as migrações**:
   - Crie e aplique as migrações para atualizar o banco de dados:
     ```bash
     python manage.py makemigrations
     python manage.py migrate
     ```

#### Parte 3: Atualizar os formulários e views para lidar com o upload de imagens

1. **Criar ou atualizar o formulário `TarefaForm`**:
   - Crie um arquivo `forms.py` dentro da aplicação `tarefas` (se ainda não existir) e defina o `TarefaForm`:
     ```python
     # tarefas/forms.py

     from django import forms
     from .models import Tarefa

     class TarefaForm(forms.ModelForm):
         class Meta:
             model = Tarefa
             fields = ['titulo', 'imagem']
     ```

2. **Modificar a view `lista_tarefas` para usar o formulário**:
   - No arquivo `views.py`, atualize a função `lista_tarefas` para lidar com o upload de imagens:
     ```python
     # tarefas/views.py

     from django.shortcuts import render, redirect
     from django.contrib.auth.decorators import login_required
     from django.contrib import messages
     from .models import Tarefa
     from .forms import TarefaForm

     @login_required
     def lista_tarefas(request):
         if request.method == 'POST':
             form = TarefaForm(request.POST, request.FILES)
             if form.is_valid():
                 tarefa = form.save(commit=False)
                 tarefa.usuario = request.user
                 tarefa.save()
                 messages.success(request, 'Tarefa adicionada com sucesso!')
                 return redirect('lista_tarefas')
             else:
                 messages.error(request, 'Erro ao adicionar a tarefa. Verifique os dados informados.')
         else:
             form = TarefaForm()

         tarefas = Tarefa.objects.filter(usuario=request.user)
         return render(request, 'tarefas/lista_tarefas.html', {'tarefas': tarefas, 'form': form})
     ```

3. **Modificar a view `editar_tarefa` para lidar com imagens**:
   - Atualize a função `editar_tarefa` para permitir a edição da imagem:
     ```python
     @login_required
     def editar_tarefa(request, id):
         tarefa = get_object_or_404(Tarefa, id=id, usuario=request.user)
         if request.method == 'POST':
             form = TarefaForm(request.POST, request.FILES, instance=tarefa)
             if form.is_valid():
                 form.save()
                 messages.success(request, 'Tarefa atualizada com sucesso!')
                 return redirect('lista_tarefas')
             else:
                 messages.error(request, 'Erro ao atualizar a tarefa. Verifique os dados informados.')
         else:
             form = TarefaForm(instance=tarefa)

         return render(request, 'tarefas/editar_tarefa.html', {'form': form})
     ```

#### Parte 4: Atualizar os templates para suportar o upload e exibição de imagens

1. **Modificar o template `lista_tarefas.html`**:
   - Atualize o template para exibir o formulário utilizando o `django-bootstrap4` e incluir o campo de imagem:
     ```html
     <!-- tarefas/templates/tarefas/lista_tarefas.html -->
     {% extends 'base.html' %}
     {% load bootstrap4 %}
     {% block title %}Lista de Tarefas{% endblock %}
     {% block content %}
     <h2>Minhas Tarefas</h2>

     <!-- Formulário para adicionar tarefas -->
     <form method="POST" enctype="multipart/form-data" class="mb-4">
         {% csrf_token %}
         {% bootstrap_form form %}
         <button type="submit" class="btn btn-primary">Adicionar</button>
     </form>

     <!-- Lista de tarefas -->
     <ul class="list-group">
         {% for tarefa in tarefas %}
             <li class="list-group-item d-flex justify-content-between align-items-center {% if tarefa.concluida %}list-group-item-success{% endif %}">
                 <div class="d-flex align-items-center">
                     {% if tarefa.imagem %}
                         <img src="{{ tarefa.imagem.url }}" alt="{{ tarefa.titulo }}" class="img-thumbnail me-2" style="width: 50px; height: 50px;">
                     {% endif %}
                     {% if tarefa.concluida %}
                         <s>{{ tarefa.titulo }}</s>
                     {% else %}
                         {{ tarefa.titulo }}
                     {% endif %}
                 </div>
                 <div>
                     {% if not tarefa.concluida %}
                         <a href="{% url 'concluir_tarefa' tarefa.id %}" class="btn btn-sm btn-success">Concluir</a>
                     {% endif %}
                     <a href="{% url 'editar_tarefa' tarefa.id %}" class="btn btn-sm btn-warning">Editar</a>
                     <a href="{% url 'excluir_tarefa' tarefa.id %}" class="btn btn-sm btn-danger" onclick="return confirmarExclusao();">Excluir</a>
                 </div>
             </li>
         {% empty %}
             <li class="list-group-item">Nenhuma tarefa adicionada.</li>
         {% endfor %}
     </ul>
     {% endblock %}
     ```

2. **Modificar o template `editar_tarefa.html`**:
   - Atualize o template para permitir a edição da imagem:
     ```html
     <!-- tarefas/templates/tarefas/editar_tarefa.html -->
     {% extends 'base.html' %}
     {% load bootstrap4 %}
     {% block title %}Editar Tarefa{% endblock %}
     {% block content %}
     <h2>Editar Tarefa</h2>
     <form method="POST" enctype="multipart/form-data">
         {% csrf_token %}
         {% bootstrap_form form %}
         <button type="submit" class="btn btn-primary">Salvar</button>
         <a href="{% url 'lista_tarefas' %}" class="btn btn-secondary">Cancelar</a>
     </form>
     {% endblock %}
     ```

#### Parte 5: Configurar o servidor para servir arquivos de mídia

1. **Atualizar as configurações no `settings.py`**:
   - Adicione as configurações para manipulação de arquivos de mídia:
     ```python
     # lista_de_tarefas/settings.py

     import os

     MEDIA_URL = '/media/'
     MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
     ```

2. **Atualizar o `urls.py` do projeto para servir arquivos de mídia no desenvolvimento**:
   - No arquivo `urls.py` do projeto principal, adicione as configurações para servir arquivos de mídia durante o desenvolvimento:
     ```python
     # lista_de_tarefas/urls.py

     from django.contrib import admin
     from django.urls import path, include
     from django.conf import settings
     from django.conf.urls.static import static

     urlpatterns = [
         path('admin/', admin.site.urls),
         path('accounts/', include('django.contrib.auth.urls')),
         path('', include('tarefas.urls')),
     ]

     if settings.DEBUG:
         urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
     ```

#### Parte 6: Testar a funcionalidade de upload de imagens

1. **Iniciar o servidor de desenvolvimento**:
   ```bash
   python manage.py runserver
