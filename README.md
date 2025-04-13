# 이 코드는 Django의 manage.py shell에서 사용할 수 있는 Book 모델을 정의합니다.

Book 모델은 책의 제목(title)과 저자(author)를 저장하며, 데이터베이스에서 책 정보를 관리하는 데 사용됩니다.

## 주요 기능

1. `__str__` 메서드: 책 객체를 문자열로 표현할 때 "제목 by 저자" 형식으로 반환합니다.
2. 클래스 메서드:
   - `get_all_books`: 데이터베이스에 저장된 모든 책 객체를 반환합니다.
   - `get_books_by_author`: 특정 저자의 이름으로 필터링된 책 객체를 반환합니다.
   - `get_books_by_title_keyword`: 제목에 특정 키워드가 포함된 책 객체를 반환합니다.
   - `get_books_ordered_by_title`: 제목을 기준으로 정렬된 책 객체를 반환합니다.

이 코드는 Django ORM을 활용하여 데이터베이스와 상호작용하며, 책 데이터를 효율적으로 조회할 수 있도록 설계되었습니다.

---

## 코드 설명

### Book 모델

`Book` 클래스는 Django의 `models.Model`을 상속받아 데이터베이스 테이블과 매핑되는 모델입니다. 이 모델은 책 데이터를 저장하고 관리하기 위한 구조를 제공합니다.

#### 필드

- `title`: 책의 제목을 저장하는 `CharField`로, 최대 길이는 200자입니다.
- `author`: 책의 저자를 저장하는 `CharField`로, 최대 길이는 100자입니다.

#### 메서드

- `__str__`: 책 객체를 문자열로 표현할 때 사용됩니다. 책의 제목과 저자를 포함한 문자열을 반환합니다. 예: `"책 제목 by 저자"`

#### 클래스 메서드

1. `get_all_books`:

   - **설명**: 데이터베이스에 저장된 모든 책 데이터를 조회합니다.
   - **반환값**: `QuerySet` 형태로 모든 책 객체를 반환합니다.

2. `get_books_by_author`:

   - **설명**: 특정 저자의 책 데이터를 조회합니다.
   - **매개변수**: `author_name` (저자 이름)
   - **반환값**: 주어진 저자 이름과 일치하는 책 객체의 `QuerySet`을 반환합니다.

3. `get_books_by_title_keyword`:

   - **설명**: 제목에 특정 키워드가 포함된 책 데이터를 조회합니다.
   - **매개변수**: `keyword` (검색 키워드)
   - **반환값**: 제목에 키워드가 포함된 책 객체의 `QuerySet`을 반환합니다.

4. `get_books_ordered_by_title`:
   - **설명**: 책 데이터를 제목의 알파벳 순서로 정렬하여 조회합니다.
   - **반환값**: 제목 기준으로 정렬된 책 객체의 `QuerySet`을 반환합니다.

---

## 코드 예제

```python
from django.db import models
from django.db.models import QuerySet

class Book(models.Model):
     title = models.CharField(max_length=200)
     author = models.CharField(max_length=100)

     def __str__(self):
          return f"{self.title} by {self.author}"

     @classmethod
     def get_all_books(cls) -> QuerySet['Book']:
          return cls.objects.all()

     @classmethod
     def get_books_by_author(cls, author_name) -> QuerySet['Book']:
          return cls.objects.filter(author=author_name)

     @classmethod
     def get_books_by_title_keyword(cls, keyword) -> QuerySet['Book']:
          return cls.objects.filter(title__icontains=keyword)

     @classmethod
     def get_books_ordered_by_title(cls) -> QuerySet['Book']:
          return cls.objects.all().order_by('title')
```

---

## 활용 예시

이 모델은 Django의 `manage.py shell`에서 다음과 같이 사용할 수 있습니다:

````python
# 모든 책 조회
books = Book.get_all_books()

# 특정 저자의 책 조회
author_books = Book.get_books_by_author("J.K. Rowling")

# 제목에 특정 키워드가 포함된 책 조회
keyword_books = Book.get_books_by_title_keyword("Python")

# 제목 기준으로 정렬된 책 조회
ordered_books = Book.get_books_ordered_by_title()
```markdown
---

## 코드 실행 예제 및 설명

아래는 `Book` 모델의 주요 메서드를 활용한 코드 예제와 각 라인에 대한 설명입니다.

### 코드 예제

```python
from books.models import Book

# 1. 전체 책 조회
all_books = Book.get_all_books()
print("📚전체 책 목록:")
for book in all_books:
    print(book)

# 2. 특정 저자 책만 조회
orwell_books = Book.get_books_by_author("George Orwell")
print("\n🖋️ George Orwell의 책 목록:")
for book in orwell_books:
    print(book)

# 3. 제목 키워드로 검색
dystopia_books = Book.get_books_by_title_keyword("new")
print("\n🔍제목에 'new'가 포함된 책 목록:")
for book in dystopia_books:
    print(book)

# 4. 제목순 정렬
sorted_books = Book.get_books_ordered_by_title()
print("\n🔠제목순 정렬:")
for book in sorted_books:
    print(book)
````

### 코드 설명

#### 1. 전체 책 조회

```python
all_books = Book.get_all_books()
```

- **설명**: 데이터베이스에 저장된 모든 책 객체를 조회합니다.
- **출력**: `📚전체 책 목록:` 이후 모든 책의 제목과 저자가 출력됩니다.

#### 2. 특정 저자 책만 조회

```python
orwell_books = Book.get_books_by_author("George Orwell")
```

- **설명**: `George Orwell`이라는 저자의 책만 필터링하여 조회합니다.
- **출력**: `🖋️ George Orwell의 책 목록:` 이후 해당 저자의 책 목록이 출력됩니다.

#### 3. 제목 키워드로 검색

```python
dystopia_books = Book.get_books_by_title_keyword("new")
```

- **설명**: 제목에 `new`라는 키워드가 포함된 책을 검색합니다.
- **출력**: `🔍제목에 'new'가 포함된 책 목록:` 이후 검색된 책 목록이 출력됩니다.

#### 4. 제목순 정렬

```python
sorted_books = Book.get_books_ordered_by_title()
```

- **설명**: 데이터베이스에 저장된 책 데이터를 제목 기준으로 알파벳 순서로 정렬합니다.
- **출력**: `🔠제목순 정렬:` 이후 제목순으로 정렬된 책 목록이 출력됩니다.

이 코드는 Django ORM을 활용하여 책 데이터를 효율적으로 조회하고 출력하는 방법을 보여줍니다.

```

```
