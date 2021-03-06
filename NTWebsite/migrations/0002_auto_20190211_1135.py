# Generated by Django 2.0.6 on 2019-02-11 03:35

import ckeditor_uploader.fields
from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
        ('NTWebsite', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attitude',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Point', models.IntegerField(verbose_name='立场代码')),
                ('EditTime', models.DateTimeField(auto_now=True, verbose_name='时间')),
                ('ObjectID', models.CharField(blank=True, max_length=50, verbose_name='ID')),
                ('Type', models.CharField(blank=True, max_length=30, verbose_name='类型')),
            ],
            options={
                'verbose_name_plural': '**3**文章立场统计**3**',
                'verbose_name': '立场记录',
            },
        ),
        migrations.CreateModel(
            name='BlackList',
            fields=[
                ('ID', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='黑名单ID')),
            ],
            options={
                'verbose_name_plural': '**3**黑名单**3**',
                'verbose_name': '记录',
            },
        ),
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Type', models.CharField(blank=True, default='T', max_length=30, verbose_name='收藏类型')),
                ('ObjectID', models.CharField(max_length=12, verbose_name='文章ID')),
                ('CollectTime', models.DateField(auto_now=True, verbose_name='时间')),
            ],
            options={
                'verbose_name_plural': '**3**文章用户收藏**3**',
                'verbose_name': '文章收藏',
            },
        ),
        migrations.CreateModel(
            name='CommentInfo',
            fields=[
                ('ObjectID', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='评论ID')),
                ('TopicID', models.CharField(default='', max_length=100, verbose_name='文章ID')),
                ('Comment', models.TextField(verbose_name='评论内容')),
                ('Parent', models.CharField(blank=True, default='', max_length=100, null=True, verbose_name='父评论ID')),
                ('Like', models.IntegerField(default='0', verbose_name='赞')),
                ('Type', models.CharField(default='T', max_length=30, verbose_name='评论归属')),
                ('Dislike', models.IntegerField(default='0', verbose_name='怼')),
                ('EditDate', models.DateTimeField(auto_now=True, verbose_name='编辑时间')),
            ],
            options={
                'verbose_name_plural': '**1**评论信息**1**',
                'verbose_name': '评论',
            },
        ),
        migrations.CreateModel(
            name='ConfigParams',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=20, unique=True, verbose_name='配置名称')),
                ('TimeOut', models.IntegerField(default=60, verbose_name='缓存时间')),
                ('ReadsThreshold', models.CharField(default=10, max_length=20, verbose_name='阅读量阈值')),
                ('TopicHotKeyWord', models.CharField(default='差评', max_length=20, verbose_name='文章热搜词')),
                ('RollCallHotKeyWord', models.CharField(default='差评', max_length=20, verbose_name='点名热搜词')),
                ('SpecialTopicHotKeyWord', models.CharField(default='差评', max_length=20, verbose_name='专题热搜词')),
                ('TopicsLimit', models.CharField(default=100, max_length=20, verbose_name='文章获取数量')),
                ('CommentsLimit', models.CharField(default=100, max_length=20, verbose_name='文章评论获取数量')),
                ('SecretKey', models.CharField(max_length=16, verbose_name='加密秘钥')),
                ('SecretVI', models.CharField(max_length=16, verbose_name='加密偏移量')),
                ('TopicsPageLimit', models.IntegerField(default=10, verbose_name='每页文章数量')),
                ('SpecialTopicsPageLimit', models.IntegerField(default=10, verbose_name='每页专题数量')),
                ('RollCallsPageLimit', models.IntegerField(default=10, verbose_name='每页点名数量')),
                ('CommentsPageLimit', models.IntegerField(default=10, verbose_name='每页评论数量')),
                ('AvatarResolution', models.IntegerField(default=102, verbose_name='头像分辨率')),
                ('PicUploadWidth', models.IntegerField(default=600, verbose_name='上传图片限制宽度')),
                ('PicUploadFormat', models.CharField(default='jpg,png', max_length=20, verbose_name='上传图片格式')),
                ('PicTempPath', models.CharField(default='TopicPicUpload/Temp/', max_length=50, verbose_name='文章临时图片路径')),
                ('PicSavePath', models.CharField(default='TopicPicUpload/Save/', max_length=50, verbose_name='文章发布图片路径')),
                ('AvatarSavePath', models.CharField(default='Avatar/', max_length=50, verbose_name='文章发布图片路径')),
                ('DefaultAvatar', models.ImageField(blank=True, default='', upload_to='Default', verbose_name='默认头像')),
            ],
            options={
                'verbose_name_plural': '**2**配置参数**2**',
                'verbose_name': '配置参数',
            },
        ),
        migrations.CreateModel(
            name='FilterQueryString',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100, verbose_name='过滤器名称')),
                ('MethodString', models.CharField(default='', max_length=200, verbose_name='使用方法')),
                ('QueryString', models.CharField(max_length=200, verbose_name='查询语句')),
                ('Template', models.CharField(max_length=100, null=True, verbose_name='使用模板')),
            ],
            options={
                'verbose_name_plural': '**2**过滤器查询语句设置**2**',
                'verbose_name': '过滤器',
            },
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('ID', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='通知ID')),
                ('Region', models.CharField(default='', max_length=100, verbose_name='目标区域')),
                ('ObjectID', models.CharField(default='', max_length=100, verbose_name='目标ID')),
                ('AnchorID', models.CharField(default='', max_length=100, verbose_name='定位ID')),
            ],
            options={
                'verbose_name_plural': '**3**通知信息**3**',
                'verbose_name': '信息',
            },
        ),
        migrations.CreateModel(
            name='PreferredConfigName',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='NTWebsite.ConfigParams', to_field='Name', verbose_name='首选配置名称')),
            ],
            options={
                'verbose_name_plural': '**2**首选配置设置**2**',
                'verbose_name': '首选配置',
            },
        ),
        migrations.CreateModel(
            name='PublisherList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Order', models.IntegerField(default=0, verbose_name='顺序')),
            ],
            options={
                'verbose_name_plural': '**3**推荐用户**3**',
                'verbose_name': '推荐用户',
            },
        ),
        migrations.CreateModel(
            name='ReadsIP',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('IP', models.CharField(blank=True, max_length=100, null=True, verbose_name='IP')),
                ('EditDate', models.DateField(auto_now=True, verbose_name='时间')),
                ('Type', models.CharField(blank=True, default='T', max_length=30, verbose_name='IP归入')),
                ('ObjectID', models.CharField(blank=True, max_length=100, null=True, verbose_name='文章ID')),
            ],
            options={
                'verbose_name_plural': '**3**文章阅读IP统计**3**',
                'verbose_name': '阅读IP记录',
            },
        ),
        migrations.CreateModel(
            name='RollCallDialogue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('EditDate', models.DateField(auto_now=True, verbose_name='编辑时间')),
                ('Query', models.CharField(default='', max_length=30, verbose_name='询问内容')),
                ('Reply', models.CharField(default='', max_length=30, verbose_name='回复内容')),
            ],
            options={
                'verbose_name_plural': '**4**点名对话明细**4**',
                'verbose_name': '对话记录',
            },
        ),
        migrations.CreateModel(
            name='RollCallInfo',
            fields=[
                ('ID', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='点名ID')),
                ('Title', models.CharField(max_length=35, unique=True, verbose_name='点名标题')),
                ('EditDate', models.DateField(auto_now=True, verbose_name='编辑时间')),
                ('LeftLike', models.IntegerField(default=0, verbose_name='点名者支持数')),
                ('RightLike', models.IntegerField(default=0, verbose_name='被点名者支持数')),
                ('Read', models.IntegerField(default=0, verbose_name='点名阅读量')),
            ],
            options={
                'verbose_name_plural': '**4**点名基础信息**4**',
                'verbose_name': '点名信息',
            },
        ),
        migrations.CreateModel(
            name='SearchIndex',
            fields=[
                ('Content', models.CharField(max_length=50000, verbose_name='匹配内容')),
                ('ID', models.CharField(default='0', max_length=12, primary_key=True, serialize=False, verbose_name='ID')),
                ('Type', models.CharField(max_length=10, unique=True, verbose_name='所属板块')),
            ],
            options={
                'verbose_name_plural': '**5**全局索引**5**',
                'verbose_name': '全局索引',
            },
        ),
        migrations.CreateModel(
            name='TipOffBox',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ObjectID', models.CharField(default='', max_length=100, verbose_name='对象ID')),
                ('Type', models.CharField(default='', max_length=30, verbose_name='对象类型')),
                ('Content', models.CharField(default='', max_length=100, verbose_name='举报内容')),
                ('EditDate', models.DateField(auto_now=True, verbose_name='编辑时间')),
            ],
            options={
                'verbose_name_plural': '**3**举报中心**3**',
                'verbose_name': '记录',
            },
        ),
        migrations.CreateModel(
            name='TopicCategoryInfo',
            fields=[
                ('Name', models.CharField(max_length=10, primary_key=True, serialize=False, verbose_name='品类名称')),
                ('SVG', models.TextField(max_length=1000, verbose_name='图标SVG')),
            ],
            options={
                'verbose_name_plural': '**5**文章类目**5**',
                'verbose_name': '类目',
            },
        ),
        migrations.CreateModel(
            name='TopicInfo',
            fields=[
                ('ObjectID', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='文章ID')),
                ('Title', models.CharField(max_length=35, unique=True, verbose_name='文章标题')),
                ('Description', models.TextField(max_length=140, verbose_name='文章描述')),
                ('Content', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='文章正文')),
                ('Type', models.CharField(default='Topic', max_length=20, verbose_name='文章类型')),
                ('Cover', models.ImageField(blank=True, default='', upload_to='Cover', verbose_name='封面图')),
                ('Recommend', models.DecimalField(decimal_places=2, default=0, max_digits=8, null=True, verbose_name='推荐度')),
                ('Like', models.IntegerField(default=0, verbose_name='赞')),
                ('Dislike', models.IntegerField(default=0, verbose_name='怼')),
                ('Hot', models.IntegerField(default=10, verbose_name='热度')),
                ('Comment', models.IntegerField(default=0, verbose_name='评论数')),
                ('Collect', models.IntegerField(default=0, verbose_name='关注或收藏量')),
                ('EditDate', models.DateField(auto_now=True, verbose_name='编辑时间')),
                ('Category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='NTWebsite.TopicCategoryInfo', verbose_name='文章类别')),
            ],
            options={
                'verbose_name_plural': '**5**文章基础信息**5**',
                'verbose_name': '文章信息',
            },
        ),
        migrations.CreateModel(
            name='TopicThemeInfo',
            fields=[
                ('Name', models.CharField(max_length=10, primary_key=True, serialize=False, verbose_name='主题名称')),
            ],
            options={
                'verbose_name_plural': '**5**文章主题标签**5**',
                'verbose_name': '主题标签',
            },
        ),
        migrations.CreateModel(
            name='UserLink',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('LinkTime', models.DateField(auto_now=True, verbose_name='时间')),
            ],
            options={
                'verbose_name_plural': '**3**用户关系网**3**',
                'verbose_name': '关注信息',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('Nick', models.CharField(max_length=20, verbose_name='昵称')),
                ('Sex', models.CharField(blank=True, default='未公开', max_length=3, verbose_name='性别')),
                ('Region', models.CharField(blank=True, default='城市', max_length=10, null=True, verbose_name='地区')),
                ('Description', models.TextField(blank=True, default='简介', max_length=50, null=True, verbose_name='简介')),
                ('Avatar', models.TextField(blank=True, default='/static/media/DefaultLogo.jpg', max_length=1000, verbose_name='头像URL')),
                ('Constellation', models.CharField(blank=True, default='天蝎座', max_length=10, null=True, verbose_name='星座')),
                ('FansCount', models.IntegerField(default=0, verbose_name='关注者数量')),
                ('FoucusCount', models.IntegerField(default=0, verbose_name='关注数量')),
                ('TCount', models.IntegerField(default=0, verbose_name='文章发布数量')),
                ('SCount', models.IntegerField(default=0, verbose_name='专题发布数量')),
                ('RCount', models.IntegerField(default=0, verbose_name='点名数量')),
                ('RRCount', models.IntegerField(default=0, verbose_name='点名回复数量')),
                ('TRCount', models.IntegerField(default=0, verbose_name='文章评论数量')),
                ('SRCount', models.IntegerField(default=0, verbose_name='专题评论数量')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name_plural': '用户信息',
                'verbose_name': '用户',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.AddField(
            model_name='userlink',
            name='UserBeLinked',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='被关注用户'),
        ),
        migrations.AddField(
            model_name='userlink',
            name='UserLinking',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='NickLinking', to=settings.AUTH_USER_MODEL, verbose_name='关注用户'),
        ),
        migrations.AddField(
            model_name='topicinfo',
            name='Publisher',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='用户名'),
        ),
        migrations.AddField(
            model_name='topicinfo',
            name='Theme',
            field=models.ManyToManyField(related_name='Topic', to='NTWebsite.TopicThemeInfo', verbose_name='文章主题标签'),
        ),
        migrations.AddField(
            model_name='tipoffbox',
            name='User',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='TipOffUser', to=settings.AUTH_USER_MODEL, verbose_name='举报用户'),
        ),
        migrations.AddField(
            model_name='rollcallinfo',
            name='Publisher',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='Publisher_User', to=settings.AUTH_USER_MODEL, verbose_name='点名者'),
        ),
        migrations.AddField(
            model_name='rollcallinfo',
            name='Target',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='Target_User', to=settings.AUTH_USER_MODEL, verbose_name='被点名者'),
        ),
        migrations.AddField(
            model_name='rollcalldialogue',
            name='ID',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='NTWebsite.RollCallInfo', verbose_name='点名信息'),
        ),
        migrations.AddField(
            model_name='publisherlist',
            name='Publisher',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='用户名'),
        ),
        migrations.AddField(
            model_name='notification',
            name='SourceUser',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='SourceUser', to=settings.AUTH_USER_MODEL, verbose_name='通知者'),
        ),
        migrations.AddField(
            model_name='notification',
            name='TargetUser',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='TargetUser', to=settings.AUTH_USER_MODEL, verbose_name='被通知者'),
        ),
        migrations.AddField(
            model_name='commentinfo',
            name='Publisher',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='用户名'),
        ),
        migrations.AddField(
            model_name='collection',
            name='User',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='用户名'),
        ),
        migrations.AddField(
            model_name='blacklist',
            name='Enforceder',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='User', to=settings.AUTH_USER_MODEL, verbose_name='被添加用户'),
        ),
        migrations.AddField(
            model_name='blacklist',
            name='Handler',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Handler', to=settings.AUTH_USER_MODEL, verbose_name='操作用户'),
        ),
        migrations.AddField(
            model_name='attitude',
            name='User',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='用户'),
        ),
    ]
