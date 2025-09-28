# App de Afiliados — Mock de Interface

Projeto React com Vite e Tailwind. Interface simulada do app de afiliados. Serve para validar a experiência antes do backend.

## Como rodar

1. Instale o Node.js LTS
2. No terminal, dentro da pasta do projeto, rode:
   ```bash
   npm install
   npm run dev
   ```
3. Abra http://localhost:5173

## Estrutura

- index.html ponto de entrada do Vite
- src/main.tsx bootstrap do React
- src/App.tsx interface mockada
- src/index.css estilos com Tailwind

## Build de produção

```bash
npm run build
npm run preview
```

## Próximos passos

- Rotas de API para scraping real
- Integração com Google Sheets
- Conversão para a planilha padrão que o Canva vai consumir
