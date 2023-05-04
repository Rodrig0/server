Para executar o projeto, primeiro é preciso executar o servidor (past server) que será o backend do web app. É recomendado rodá-lo na porta 5004 que é a porta configurada no frontend:


```
flask run -p 5004
```

A API poderá ser acessada com o endpoints abaixo:

```
http://localhost:5004/books
http://localhost:5004/books/<string:book_id>
```

Para visualizar o swagger basta acessar a URL abaixo:

```
http://127.0.0.1:5004/swagger-ui
```
Em seguida, execute o passos descritos no readme do frontend (client) para inicializar o web app.
