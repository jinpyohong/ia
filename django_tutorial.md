
# Django Tutorial
[See Django 2.2 Documentation Contents]( https://docs.djangoproject.com/en/2.2/contents/)

## Install Django
### Python Virtual Environment 구축
#### PyCharm IDE에서
Create New Project:
> Project Interpreter를 `Virtualenv`를 선택하고 Base interpreter를 선택한다.
 (이전에 만든 virtualenv도 필요하면 선택할 수 있다. 이것을 재사용함)

Source를 GitHub 등에서 clone해서 가져왔을 때, Open:
> File >> Settings >> Poject >> Project interpreter: 설정 아이콘을 클릭하고 `Add...`를 선택하여 Virtual Environment를 설정한다. (Create New Project에서와 동일)

#### Command line에서

Current directory에 Python 가상환경이 설치될 directory 명을 `myenv`라 하자.
`venv`라는 가상환경 생성해 주는 module(Python3.4 이상에서 포함됨)을 실행시키자.  
```
> python -m venv myenv
```
그러면, myenv directory 하부에 새로운 python.exe가 설치되고, site-packeges/ 밑에 pip와 setuptool만 설치된다. 

가상환경을 활성화한다. (사실은 환경변수 PATH와 PYTHONPATH를 venv를 사용하도록 조정하는 것이다.)

Windows:
```
> myenv\Scripts\activate.bat
(myenv) > 
```
Linux:
```
$ source myenv/bin/activate
(myenv) $
```
(myenv) 프롬프트가 생기면, 이제부터 virtual environenment이 적용된다. 즉, python version도 지정되었고, 추가 설치되는 package들도 이 환경에서만 독립적으로 설치되고 영향을 준다. 다시 말해, 이전에 사용한 시스템 python 인터프리터와 package에 영향을 주고 받지 않는 나만의 고유 환경을 구성할 수 있다. 

사용자 code와 package간, 또는 package간에 dependency가 있는 경우에 유용하며, 다른 기계로 porting하기 편리하다.

가상환경을 비활성화 시키려면(끝내려면),

Windows:
```
(myenv) > deactivate.bat
>
```
Linux:
```
(myenv) $ deactivate
$
```

Python을 실행시켜 `sys.path`를 확인해 보자. Module을 찾을 path를 확인해 보자.

### Virtual env에서 Django package 설치하기

#### PyCharm IDE에서
> File >> Settings >> Poject >> Project interpreter: site-packages directory에 설치된 pip와 setup tools가 list되어 있다. 이제 새 package를 설치하려면, `+`를 누르고
`django`를 검색해 보자. `Django`를 선택해서 `Install Package`를 클릭. 
특정 version을 선택할 수도 있다. -->` Specify version` 칸에 version 번호를 입력

#### Command line에서
```
> pip install Django
```

Django 1.11.20 version을 설치하려면,
```
> pip install Django==1.11.20
```

Note: 이 가상환경에서 설치된 package들은 기존에 설치된 Python interpreter에 영향을 주지 않는다.

## Setup a database
PostgreSQL, MySQL, or Oracle 등 대형 DBMS:
- 별도 설치가 필요하다. 
- 이 DBMS는 application server와 별도의 machine에서 실행 가능하며 TCP socket 통신으로 query가 전달된다. 
- 물론, 사용권한이 있어야 한다.
- Python interface를 위한 DB API 설치 필요

참고: Python MySQL https://www.w3schools.com/python/python_mysql_getstarted.asp

SQLite3:
- Django의 default DB이며 표준 Python에 포함되어 있다. 
- 다만, SQL을 사용하지 않고 DB를 access하려면, [SQLite Database Browser](https://sqlitebrowser.org/)를 설치하자.

## Django at a glance
See https://docs.djangoproject.com/en/2.2/intro/overview/

![image.png](attachment:image.png)


## [Writing your first Django app, part 1](https://docs.djangoproject.com/en/2.2/intro/tutorial01/)
1. Creating a project
2. The development server
3. Creating the Polls app
4. Write your first view
