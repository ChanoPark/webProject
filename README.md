## 📣한마음 고대 프로젝트 (2021/05~2021/06)  
제 하루의 일상은 노트북의 작은 화면에서 시작합니다. 장학금 정보, 취업 정보 등 많은 정보를 얻기 위해 다양한 홈페이지를 돌아다니며 하루가 시작됩니다.
어느날, 여러 홈페이지에 있는 정보를 한 곳에 모아주는 홈페이지가 있으면 어떨까? 라는 생각이 들었습니다. 사소한 불편함을 해소하고자 하는 마음이 학교의 다양한 정보가 모여있는 웹 페이지, **한마음 고대** 프로젝트의 시작입니다. 

---

### 1️⃣프로젝트 개요

학교는 많은 정보를 학생에게 제공하지만, 정보를 제대로 활용하는 학생은 많지 않습니다. 그 이유는 다음과 같이 유추할 수 있습니다.

- 정보를 제공하는 홈페이지가 산발적으로 존재
- COVID-19로 인한 선·후배간 교류 단절

학생들에게 필요한 정보는 인재 양성 센터, 대학 일자리 센터, 포털 등 다양한 홈페이지에 분산되어 있습니다. 학생들은 언제 올라올지 모르는 새로운 정보를 얻기 위해
매일같이 여러 홈페이지를 북마크에 등록하고 확인합니다. COVID-19 이전, 대면 수업이 진행되어 학교에 수업을 들으러 올 땐 벽보, 게시판 등 자연스럽게 정보를 얻을 수단이
존재했지만, 비대면 수업이 진행되는 현상황은 그렇지 않습니다. 학생들은 하루에도 여러 번 같은 사이트를 접속해야 하는 불편함을 감수해야 합니다.
또한, 비대면 수업의 장기화로 인해 동기 및 선·후배간 교류가 일어나고 있지 않습니다. 누군가는 정보 제공 사이트의 존재조차 모르며, 신입생은 주변의 도움도 받지 못한 채, 정보의 바다에서 빠져 헤어나오지 못하고 있습니다.

따라서, 저는 위와 같은 문제를 해결하기 위한 한마음 고대를 기획하게 되었습니다.

---

### 2️⃣문제 해결 방안 및 요구 사항
🔥**학생에게 필요한 정보를 한 곳에 모으고 정보를 공유할 수 있는 웹 사이트 개발**🔥  

**1. 기능 요구사항**
- 공지사항 등 **정적**인 정보는 HTML 문서로 작성해 제공
- 채용공고 등 **동적**인 정보는 웹 크롤링(Crawling)을 통해 제공
- 사이트 외 추가 정보를 공유할 수 있는 게시판 기능 제공  

**2. 비기능 요구사항** 
- 개발 기한 엄수
- 최신 정보를 우선으로 제공(내림차순 정렬)
- 출처 명시

---

### 3️⃣개발 도구
- Full Stack(Back-end, Front-end) : **Django Framework** (Python, HTML, Template language)  
- Datadase&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
: **Sqlite3**  
- Using library&nbsp;&nbsp;　&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
: **Beautiful soup4**(for crawling), **matrial Design/Bootstrap**(for css)  

---

### 4️⃣디자인 패턴
디자인 패턴은 효율적으로 소프트웨어를 개발하고, 그 과정에서 발생할 수 있는 문제를 쉽게 해결할 수 있는 **설계 구조**입니다.  

📖Django의 Document에 따르면, `Loose coupling(낮은 결합도)`와 `tight cohesion(높은 응집도)`를 지향하며, 프레임워크의 각 계층은 정말로 필요하기 전에는 서로 "몰라야 한다"고 말하고 있습니다. 
따라서, 각 **Model**, **Template**, **View**는 서로 분리되어 있고, **URLConf**를 통해 연결됩니다. 이와 같이, **각각의 구성 요소가 다른 요소들에게 영향을 미치지 않아야 한다**는 것에 입각한 `MTV pattern`을 사용하고 있습니다.  
MTV패턴은 MVC패턴에 입각하여 만들어진 디자인 패턴으로, 구성 요소는 다음과 같습니다.
Layer | Description 
------------ | ------------- 
**Model**| MVC패턴의 Model에 대응되며, DB에 저장되는 데이터를 뜻합니다.<br> Model은 클래스로 정의되며, 각 클래스는 ORM 기술을 통해 Table에 매핑됩니다. 
**Template**| MVC패턴의 View에 대응되며, 유저에게 보여지는 화면을 뜻합니다.<br> View에서 로직을 처리하고 HTML 파일을 Context와 함께 렌더링하는데, 이 때 HTML 파일을 템플릿이라 합니다. 
**View** | MVC패턴의 Controller에 대응되며, 유저의 요청에 따라 적절한 로직을 수행하여 결과를 Template으로 렌더링하여 응답합니다. 
**URLConf** | URL 패턴을 정의하여, 사용자가 요청한 URL과 알맞은 View를 매핑합니다.

MTV패턴을 기반으로 각 레이어가 동작하는 방식을 그림으로 나타내면 다음과 같습니다.

<img src = "https://user-images.githubusercontent.com/77626299/165474065-e6da2ad7-ebfb-4b2a-9113-67213281db84.png" width="80%" height="80%">  

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`MTV패턴 동작과정`  

1. 유저가 URL에 요청을 보내면 URLConf에 지정된 URL패턴에 따라, 알맞은 View를 호출하게 됩니다.  
2. View는 요청에 따라 로직을 수행하게 되며 그 과정에서 발생한 데이터 처리를 Model에게 지시합니다.  
3. Model은 ORM기술에 따라 DB와 트랜잭션을 주고 받습니다.  
4. 이후, View는 결과에 따라 Template을 렌더링하여 사용자에게 Response를 넘깁니다.  

##### *ORM(Object Releation Mapping) : 객체와 테이블을 매핑하는 기술입니다. 각 Model은 클래스의 객체로 생성되고, 해당 객체를 DB의 <br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;테이블과 연결합니다. 모든 SQL을 작성하지 않아도 되므로 비즈니스 로직에 더욱 집중할 수 있다&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
<br>는 장점이 있습니다.

---

### 5️⃣프로젝트 결과 및 얻은 것  
<img src = "https://user-images.githubusercontent.com/77626299/165500760-7ca32375-03f8-46db-87cc-67b6b015df13.gif" width="50%" height="50%">  

#### 프로젝트 결과
- 정적 정보 제공 : 장학금 정보
- 동적 정보 제공 : 대외활동, 취업정보, 학사정보
- 게시판(Create, Read) 기능
- 우측 상단 퀵 메뉴 기능
- 반응형 웹 및 레이아웃 구성  

#### 경험
개발자에게 있어서, 자신이 직면한 문제를 기술적으로 해결한 경험은 매우 중요한 경험이라고 생각합니다. 비록 사소한 불편함을 해결한 것이지만, 
혼자서 무언가를 완성해냈다는 뿌듯함은 어루 말할 수 없습니다. 아직은 부끄러운 코드지만, 가까운 미래에 개발 능력이 향상되면 더 좋은 것을 만들 수 있다는 것에 설렘을 느낄 수 있었습니다.
이번 프로젝트를 통해, 추후 학습 방향과 진로에 대한 확신을 가질 수 있었습니다.

#### 개발 능력
- Django 프레임워크를 사용한 웹 사이트 개발의 전체적인 아키텍쳐 이해
- 디자인 패턴(MTV)의 이해와 적용
- 프론트 구성을 위한 HTML, CSS와 Django Template Language 이해
- 웹 크롤링을 위한 Beautiful Soup 라이브러리 및 외부 CSS 라이브러리 사용법
