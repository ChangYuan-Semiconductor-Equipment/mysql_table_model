# mysql_table_model
mysql 数据库表模型

### 更新数据库表结构

#### 1.编辑环境文件: 在alembic/env.py文件中, 导入模型并将目标元数据传递给Alembic.

```python
from mysql_table_model.semikron import BASE  # 导入您的模型模块
target_metadata = BASE.metadata  # 使用您的模型类的Base.metadata
```
#### 2.生成迁移脚本
```shell
alembic revision --autogenerate -m "add new column to table"
```
#### 3.应用迁移
```shell
alembic upgrade head
```