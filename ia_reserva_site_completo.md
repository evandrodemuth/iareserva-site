# IA Reserva — Todas as Alterações do Site
> Aplicar em ordem. Cada bloco indica exatamente **onde inserir** e traz o **código completo** pronto para uso.

---

## ESTRUTURA ATUAL (referência antes de alterar)

```
1.  HERO
2.  CONTEXTO        → "O crescimento do setor está limitado."
3.  PROBLEMAS       → "O caos invisível do atendimento"
4.  CUSTO HUMANO    → "Quanto custa manter o modelo antigo?"
5.  SOLUÇÃO         → "A automação que libera sua equipe..."
6.  COMPARATIVO     → "Comparativo Financeiro"
7.  COMO FUNCIONA   → "Experiência simples. Tecnologia completa."
8.  DASHBOARD       → "Controle completo. Resultados visíveis."
9.  PREÇOS          → "Investimento inteligente. Retorno previsível."
10. FOOTER
```

## ESTRUTURA FINAL (após todas as alterações)

```
1.  HERO                    ← ALTERAR CTAs + adicionar banner de urgência
2.  PROVA SOCIAL            ← NOVO
3.  CONTEXTO                ← manter
4.  PROBLEMAS               ← manter
5.  POSICIONAMENTO          ← NOVO
6.  CUSTO HUMANO            ← manter
7.  SOLUÇÃO                 ← manter
8.  COMPARATIVO             ← manter
9.  DEPOIMENTOS             ← NOVO
10. COMO FUNCIONA           ← manter
11. LIVIA                   ← NOVO
12. DASHBOARD               ← ALTERAR card "Rastreio de Ads"
13. PIXEL                   ← NOVO
14. PREÇOS                  ← SUBSTITUIR seção inteira
15. FAQ                     ← NOVO
16. FOOTER                  ← manter
```

---

## ALTERAÇÃO 1 — Hero: Reformular CTAs e adicionar urgência

**Onde:** Seção `#hero` atual — localizar os dois botões "Começar agora" e "Falar com a LivIA"  
**Ação:** Substituir os dois CTAs e adicionar banner de urgência logo abaixo

### Remover:
```html
<a href="#ativar">Começar agora</a>
<a href="https://app.iareserva.com.br/iareserva">Falar com a LivIA</a>
```

### Inserir no lugar:
```html
<div class="hero-ctas">
  <a href="https://app.iareserva.com.br/iareserva" class="btn-hero-primary">
    Falar com a LivIA agora →
  </a>
  <a href="#contato" class="btn-hero-secondary">
    ou agendar uma demonstração
  </a>
</div>

<div class="urgency-banner">
  ⏰ Oferta especial para os <strong>100 primeiros restaurantes</strong>
  — Setup com 50% de desconto
</div>
```

### CSS:
```css
.hero-ctas {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  gap: 12px;
  margin-top: 32px;
}
.btn-hero-primary {
  background: #E53935;
  color: white;
  padding: 16px 32px;
  border-radius: 8px;
  font-size: 1rem;
  font-weight: 700;
  text-decoration: none;
  display: inline-block;
  transition: background 0.2s;
}
.btn-hero-primary:hover {
  background: #C62828;
}
.btn-hero-secondary {
  color: #1A237E;
  font-size: 0.9rem;
  text-decoration: underline;
  opacity: 0.8;
}
.urgency-banner {
  background: #FFF8E1;
  border: 1px solid #FFE082;
  border-radius: 8px;
  padding: 10px 20px;
  font-size: 0.85rem;
  color: #E65100;
  margin-top: 20px;
  display: inline-block;
}
```

---

## ALTERAÇÃO 2 — Inserir: Barra de Prova Social

**Onde:** Inserir logo após a seção `#hero`, antes de "O crescimento do setor está limitado."  
**Ação:** Adicionar seção nova completa

```html
<!-- ========== INÍCIO: BARRA DE PROVA SOCIAL ========== -->
<section id="prova-social" class="social-proof-bar">
  <div class="proof-grid">

    <div class="proof-item">
      <span class="proof-number">+1.200</span>
      <span class="proof-label">Reservas automatizadas</span>
    </div>

    <div class="proof-item">
      <span class="proof-number">84%</span>
      <span class="proof-label">Economia vs. atendente humano</span>
    </div>

    <div class="proof-item">
      <span class="proof-number">24h</span>
      <span class="proof-label">Atendimento sem interrupção</span>
    </div>

    <div class="proof-item">
      <span class="proof-number">&lt;30s</span>
      <span class="proof-label">Para confirmar uma reserva</span>
    </div>

  </div>
</section>
<!-- ========== FIM: BARRA DE PROVA SOCIAL ========== -->
```

### CSS:
```css
.social-proof-bar {
  background: #1A237E;
  padding: 32px 0;
}
.proof-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  text-align: center;
  max-width: 1100px;
  margin: 0 auto;
  padding: 0 24px;
}
.proof-item {
  border-right: 1px solid rgba(255, 255, 255, 0.15);
  padding: 0 24px;
}
.proof-item:last-child {
  border-right: none;
}
.proof-number {
  display: block;
  font-size: 2.5rem;
  font-weight: 800;
  color: #FFFFFF;
  line-height: 1;
}
.proof-label {
  display: block;
  font-size: 0.85rem;
  color: rgba(255, 255, 255, 0.7);
  margin-top: 6px;
}

@media (max-width: 768px) {
  .proof-grid {
    grid-template-columns: repeat(2, 1fr);
    gap: 32px;
  }
  .proof-item {
    border-right: none;
  }
}
```

> **Nota:** Substitua os números pelos dados reais assim que disponíveis. Alternativas se o volume ainda for baixo: "+500 reservas", "60% redução de no-show", "8.760h de atendimento/ano" (24h × 365 dias).

---

## ALTERAÇÃO 3 — Inserir: Posicionamento para Pequenos Restaurantes

**Onde:** Inserir após "O caos invisível do atendimento" e antes de "Quanto custa manter o modelo antigo?"  
**Ação:** Adicionar seção nova completa

```html
<!-- ========== INÍCIO: POSICIONAMENTO ========== -->
<section id="para-voce" class="positioning-section">
  <div class="positioning-container">

    <div class="positioning-content">
      <span class="positioning-tag">Feito para restaurantes independentes</span>
      <h2>Você compete com grandes redes.<br>Agora tem a tecnologia delas.</h2>
      <p>
        Se você tem entre 1 e 5 unidades, uma equipe pequena e sente que perde
        reservas porque não consegue atender tudo — a IA Reserva foi construída
        exatamente para você.
      </p>
      <ul class="positioning-list">
        <li>✅ Sem contratos longos ou burocracia</li>
        <li>✅ Implantação em menos de 7 dias</li>
        <li>✅ Suporte humano — não robô de atendimento</li>
        <li>✅ Tecnologia de ponta no tamanho certo para o seu negócio</li>
      </ul>
    </div>

    <div class="positioning-callout">
      <p>"Grandes redes têm equipes inteiras de atendimento.</p>
      <p>Você não precisa delas.</p>
      <p class="callout-highlight">Precisa da LivIA."</p>
    </div>

  </div>
</section>
<!-- ========== FIM: POSICIONAMENTO ========== -->
```

### CSS:
```css
.positioning-section {
  background: #1A237E;
  padding: 80px 0;
  color: white;
}
.positioning-container {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 64px;
  align-items: center;
  max-width: 1100px;
  margin: 0 auto;
  padding: 0 24px;
}
.positioning-tag {
  background: rgba(255, 255, 255, 0.15);
  color: white;
  font-size: 0.8rem;
  font-weight: 600;
  padding: 6px 16px;
  border-radius: 20px;
  display: inline-block;
  margin-bottom: 16px;
  border: 1px solid rgba(255, 255, 255, 0.3);
  text-transform: uppercase;
  letter-spacing: 0.04em;
}
.positioning-content h2 {
  color: white;
  margin-bottom: 16px;
}
.positioning-content p {
  color: rgba(255, 255, 255, 0.8);
  line-height: 1.7;
}
.positioning-list {
  list-style: none;
  padding: 0;
  margin-top: 24px;
}
.positioning-list li {
  padding: 10px 0;
  color: rgba(255, 255, 255, 0.9);
  font-size: 0.95rem;
  border-bottom: 1px solid rgba(255, 255, 255, 0.1);
}
.positioning-callout {
  background: rgba(255, 255, 255, 0.08);
  border: 1px solid rgba(255, 255, 255, 0.2);
  border-radius: 16px;
  padding: 40px;
  text-align: center;
}
.positioning-callout p {
  font-size: 1.3rem;
  font-weight: 600;
  color: white;
  line-height: 1.8;
  margin: 0;
}
.callout-highlight {
  color: #FF6B6B !important;
  font-size: 1.5rem !important;
  margin-top: 8px !important;
}

@media (max-width: 768px) {
  .positioning-container {
    grid-template-columns: 1fr;
    gap: 40px;
  }
}
```

---

## ALTERAÇÃO 4 — Inserir: Depoimentos

**Onde:** Inserir após "Comparativo Financeiro" e antes de "Experiência simples. Tecnologia completa."  
**Ação:** Adicionar seção nova completa

```html
<!-- ========== INÍCIO: DEPOIMENTOS ========== -->
<section id="depoimentos" class="testimonials-section">
  <div class="testimonials-container">

    <h2>O que donos de restaurante dizem</h2>

    <div class="testimonials-grid">

      <div class="testimonial-card">
        <div class="testimonial-quote">"</div>
        <blockquote>
          Antes eu perdia reserva toda semana porque o telefone ficava ocupado.
          Agora a LivIA atende a madrugada e acordo com reservas confirmadas
          sem ter visto nenhuma mensagem.
        </blockquote>
        <div class="testimonial-author">
          <div class="author-avatar">JM</div>
          <div>
            <strong>João Menezes</strong>
            <span>Dono — Restaurante Varanda, São Paulo</span>
          </div>
        </div>
      </div>

      <div class="testimonial-card">
        <div class="testimonial-quote">"</div>
        <blockquote>
          Reduziu nosso no-show em mais da metade no primeiro mês. A conta fecha:
          pago menos de R$ 300 por mês e recuperei o equivalente a 6 mesas por
          fim de semana que antes ficavam vazias.
        </blockquote>
        <div class="testimonial-author">
          <div class="author-avatar">ML</div>
          <div>
            <strong>Maria Lima</strong>
            <span>Gerente — Bistrô Raízes, Curitiba</span>
          </div>
        </div>
      </div>

      <div class="testimonial-card">
        <div class="testimonial-quote">"</div>
        <blockquote>
          Minha agência instalou o pixel e agora a gente sabe exatamente qual
          campanha trouxe qual reserva. Nunca tivemos esse nível de controle
          sobre o marketing do restaurante.
        </blockquote>
        <div class="testimonial-author">
          <div class="author-avatar">RS</div>
          <div>
            <strong>Rafael Souza</strong>
            <span>Proprietário — Casa do Chef, Belo Horizonte</span>
          </div>
        </div>
      </div>

    </div>
  </div>
</section>
<!-- ========== FIM: DEPOIMENTOS ========== -->
```

### CSS:
```css
.testimonials-section {
  background: white;
  padding: 80px 0;
}
.testimonials-container {
  max-width: 1100px;
  margin: 0 auto;
  padding: 0 24px;
  text-align: center;
}
.testimonials-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 24px;
  margin-top: 48px;
  text-align: left;
}
.testimonial-card {
  background: #F8F9FF;
  border: 1px solid #E8EAFF;
  border-radius: 16px;
  padding: 32px;
  position: relative;
}
.testimonial-quote {
  font-size: 4rem;
  color: #E53935;
  font-weight: 800;
  line-height: 1;
  margin-bottom: -8px;
  font-family: Georgia, serif;
}
.testimonial-card blockquote {
  font-size: 0.95rem;
  color: #333;
  line-height: 1.7;
  margin: 0 0 24px;
  font-style: italic;
}
.testimonial-author {
  display: flex;
  align-items: center;
  gap: 12px;
}
.author-avatar {
  width: 42px;
  height: 42px;
  border-radius: 50%;
  background: #E53935;
  color: white;
  font-size: 0.75rem;
  font-weight: 700;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
}
.testimonial-author strong {
  display: block;
  font-size: 0.9rem;
  color: #1A237E;
}
.testimonial-author span {
  font-size: 0.8rem;
  color: #777;
}

@media (max-width: 768px) {
  .testimonials-grid {
    grid-template-columns: 1fr;
  }
}
```

> **⚠️ IMPORTANTE:** Substitua pelos depoimentos reais dos seus clientes assim que possível. Se ainda não tiver clientes no setor, use uma das alternativas:
> - **Opção A:** Ofereça 3 meses gratuitos em troca de depoimento em vídeo
> - **Opção B:** Substitua por dados de piloto: *"Em nosso piloto, reduzimos 65% dos no-shows nos primeiros 30 dias."*

---

## ALTERAÇÃO 5 — Inserir: Seção da LivIA

**Onde:** Inserir após "Experiência simples. Tecnologia completa." e antes de "Controle completo. Resultados visíveis."  
**Ação:** Adicionar seção nova completa

```html
<!-- ========== INÍCIO: SEÇÃO LIVIA ========== -->
<section id="livia" class="livia-section">
  <div class="livia-container">

    <div class="livia-header">
      <span class="livia-badge">Conheça a LivIA</span>
      <h2>Sua atendente que nunca falta,<br>nunca cansa e nunca erra.</h2>
      <p>
        A LivIA é a inteligência artificial da IA Reserva. Ela entende mensagens
        em linguagem natural, checa sua disponibilidade em tempo real e confirma
        reservas em menos de 30 segundos — sem que você precise tocar no celular.
      </p>
    </div>

    <div class="livia-content">

      <div class="livia-understands">
        <h3>Ela entende do jeito que o cliente fala:</h3>
        <ul class="chat-examples">
          <li>"Mesa para 4 hoje às 20h"</li>
          <li>"Quero reservar pro meu aniversário sábado"</li>
          <li>"Tem vaga pra amanhã à noite?"</li>
          <li>"Precisamos de espaço para 10 pessoas"</li>
          <li>"Pode ser às 21h30?"</li>
        </ul>
        <p class="livia-note">
          Quando não consegue resolver, ela avisa você —
          sem deixar o cliente esperando.
        </p>
      </div>

      <div class="livia-capabilities">

        <div class="capability-item">
          <span class="capability-icon">🧠</span>
          <div>
            <strong>Entende linguagem natural</strong>
            <p>Erros de digitação, abreviações e mensagens informais. Sem formulários.</p>
          </div>
        </div>

        <div class="capability-item">
          <span class="capability-icon">⚡</span>
          <div>
            <strong>Checa disponibilidade em tempo real</strong>
            <p>Consulta seu inventário de mesas no momento exato da mensagem.</p>
          </div>
        </div>

        <div class="capability-item">
          <span class="capability-icon">✅</span>
          <div>
            <strong>Confirma e envia voucher</strong>
            <p>Tudo dentro do WhatsApp. Sem apps extras, sem links externos.</p>
          </div>
        </div>

        <div class="capability-item">
          <span class="capability-icon">🔁</span>
          <div>
            <strong>Transfere quando necessário</strong>
            <p>Você define as regras. Reclamações e casos especiais vão direto para você.</p>
          </div>
        </div>

      </div>
    </div>
  </div>
</section>
<!-- ========== FIM: SEÇÃO LIVIA ========== -->
```

### CSS:
```css
.livia-section {
  background: #F8F9FF;
  padding: 80px 0;
}
.livia-container {
  max-width: 1100px;
  margin: 0 auto;
  padding: 0 24px;
}
.livia-badge {
  background: #E53935;
  color: white;
  font-size: 0.75rem;
  font-weight: 700;
  padding: 6px 16px;
  border-radius: 20px;
  letter-spacing: 0.05em;
  text-transform: uppercase;
  display: inline-block;
  margin-bottom: 16px;
}
.livia-header {
  text-align: center;
  max-width: 640px;
  margin: 0 auto 56px;
}
.livia-header h2 {
  margin-bottom: 16px;
}
.livia-header p {
  color: #555;
  line-height: 1.7;
}
.livia-content {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 56px;
  align-items: start;
}
.livia-understands h3 {
  font-size: 1rem;
  color: #1A237E;
  margin-bottom: 20px;
}
.chat-examples {
  list-style: none;
  padding: 0;
  margin: 0 0 24px;
}
.chat-examples li {
  background: white;
  border: 1px solid #E0E0E0;
  border-radius: 12px 12px 12px 4px;
  padding: 12px 16px;
  margin-bottom: 10px;
  font-size: 0.95rem;
  color: #333;
  font-style: italic;
}
.chat-examples li::before {
  content: "💬 ";
}
.livia-note {
  font-size: 0.9rem;
  color: #777;
  font-style: italic;
  padding: 12px 16px;
  background: #FFF8E1;
  border-left: 3px solid #FFD54F;
  border-radius: 4px;
}
.capability-item {
  display: flex;
  gap: 16px;
  align-items: flex-start;
  margin-bottom: 28px;
  padding-bottom: 28px;
  border-bottom: 1px solid #EEEEEE;
}
.capability-item:last-child {
  border-bottom: none;
  margin-bottom: 0;
  padding-bottom: 0;
}
.capability-icon {
  font-size: 1.6rem;
  flex-shrink: 0;
  margin-top: 2px;
}
.capability-item strong {
  display: block;
  color: #1A237E;
  font-size: 0.95rem;
  margin-bottom: 4px;
}
.capability-item p {
  margin: 0;
  color: #666;
  font-size: 0.88rem;
  line-height: 1.5;
}

@media (max-width: 768px) {
  .livia-content {
    grid-template-columns: 1fr;
    gap: 40px;
  }
}
```

---

## ALTERAÇÃO 6 — Atualizar: Card "Rastreio de Ads" no Dashboard

**Onde:** Dentro da seção "Controle completo. Resultados visíveis." — localizar o item/tab "Rastreio de Ads"  
**Ação:** Substituir o conteúdo do card por versão expandida

```html
<!-- SUBSTITUIR o card/tab "Rastreio de Ads" por: -->
<div class="feature-card feature-card--pixel">
  <span class="feature-card-icon">📡</span>
  <h4>Pixel de Rastreamento</h4>
  <p>
    Instale o pixel do Meta, Google ou qualquer plataforma diretamente na
    sua página de reservas personalizada. Rastreie visitas, conversões e
    crie campanhas de remarketing com dados reais de cada campanha.
  </p>
  <span class="feature-exclusive-badge">Exclusivo IA Reserva</span>
</div>
```

### CSS:
```css
.feature-card--pixel {
  border: 2px solid #E53935;
  position: relative;
}
.feature-exclusive-badge {
  display: inline-block;
  background: #E53935;
  color: white;
  font-size: 0.7rem;
  font-weight: 700;
  padding: 3px 10px;
  border-radius: 10px;
  margin-top: 12px;
  letter-spacing: 0.04em;
  text-transform: uppercase;
}
```

---

## ALTERAÇÃO 7 — Inserir: Seção Dedicada ao Pixel

**Onde:** Inserir após "Controle completo. Resultados visíveis." e antes da seção de preços  
**Ação:** Adicionar seção nova completa

```html
<!-- ========== INÍCIO: SEÇÃO PIXEL ========== -->
<section id="pixel" class="pixel-section">
  <div class="pixel-container">

    <div class="pixel-header">
      <span class="pixel-badge">Exclusivo — nenhum concorrente oferece isso</span>
      <h2>Pixel de rastreamento.<br>Sua agência vai adorar.</h2>
      <p>
        Cada restaurante recebe uma página de reservas personalizada onde é possível
        instalar o pixel do Meta, Google ou qualquer outra plataforma de anúncios.
        Feche o ciclo completo: do anúncio à reserva confirmada, com dados reais.
      </p>
    </div>

    <div class="pixel-features">

      <div class="pixel-feature">
        <span class="pixel-feature-icon">📊</span>
        <div>
          <h4>Visitantes da página</h4>
          <p>
            Saiba quantas pessoas acessaram sua página de reservas, em qual horário
            e de qual origem — anúncio, Instagram, Google ou link direto.
          </p>
        </div>
      </div>

      <div class="pixel-feature">
        <span class="pixel-feature-icon">✅</span>
        <div>
          <h4>Conversões reais</h4>
          <p>
            Evento de conversão disparado automaticamente quando a reserva é confirmada.
            Alimenta o pixel do Meta ou Google com dados precisos.
          </p>
        </div>
      </div>

      <div class="pixel-feature">
        <span class="pixel-feature-icon">🎯</span>
        <div>
          <h4>Remarketing preciso</h4>
          <p>
            Crie audiências de quem visitou sua página mas não reservou.
            Anuncie só para esse público — sem gastar com quem já é cliente.
          </p>
        </div>
      </div>

      <div class="pixel-feature">
        <span class="pixel-feature-icon">💰</span>
        <div>
          <h4>ROI de cada campanha</h4>
          <p>
            Saiba exatamente quanto investiu e quantas mesas vieram de cada
            anúncio. Custo por reserva adquirida, claro e mensurável.
          </p>
        </div>
      </div>

    </div>

    <div class="pixel-agency-callout">
      🤝 <strong>Tem agência de marketing?</strong> Compartilhe esta página com ela.
      A IA Reserva foi construída para trabalhar junto com quem cuida do seu marketing digital.
    </div>

  </div>
</section>
<!-- ========== FIM: SEÇÃO PIXEL ========== -->
```

### CSS:
```css
.pixel-section {
  background: white;
  padding: 80px 0;
}
.pixel-container {
  max-width: 1100px;
  margin: 0 auto;
  padding: 0 24px;
}
.pixel-badge {
  background: #E53935;
  color: white;
  font-size: 0.75rem;
  font-weight: 700;
  padding: 6px 16px;
  border-radius: 20px;
  display: inline-block;
  margin-bottom: 16px;
  text-transform: uppercase;
  letter-spacing: 0.05em;
}
.pixel-header {
  text-align: center;
  max-width: 600px;
  margin: 0 auto 56px;
}
.pixel-header p {
  color: #555;
  line-height: 1.7;
  margin-top: 16px;
}
.pixel-features {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 24px;
  max-width: 860px;
  margin: 0 auto;
}
.pixel-feature {
  display: flex;
  gap: 20px;
  align-items: flex-start;
  background: #F8F9FF;
  border: 1px solid #E8EAFF;
  border-radius: 16px;
  padding: 28px;
}
.pixel-feature-icon {
  font-size: 2rem;
  flex-shrink: 0;
}
.pixel-feature h4 {
  margin: 0 0 8px;
  color: #1A237E;
  font-size: 1rem;
}
.pixel-feature p {
  margin: 0;
  color: #555;
  font-size: 0.9rem;
  line-height: 1.6;
}
.pixel-agency-callout {
  max-width: 620px;
  margin: 40px auto 0;
  background: #FFF8E1;
  border: 1px solid #FFE082;
  border-radius: 12px;
  padding: 20px 28px;
  text-align: center;
  color: #555;
  font-size: 0.95rem;
  line-height: 1.6;
}

@media (max-width: 768px) {
  .pixel-features {
    grid-template-columns: 1fr;
  }
}
```

---

## ALTERAÇÃO 8 — Substituir: Seção de Preços

**Onde:** Seção "Investimento inteligente. Retorno previsível." (seção atual de preços)  
**Ação:** Substituir o HTML da seção inteira pelo bloco abaixo

```html
<!-- ========== INÍCIO: PREÇOS — SUBSTITUIR SEÇÃO INTEIRA ========== -->
<section id="precos" class="pricing-section">
  <div class="pricing-container">

    <div class="pricing-header">
      <span class="pricing-badge">🎯 Oferta para os 100 primeiros restaurantes</span>
      <h2>Investimento inteligente.<br>Retorno previsível.</h2>
      <p>Transparência total. Sem surpresas no boleto.</p>
    </div>

    <div class="pricing-grid">

      <div class="pricing-card">
        <div class="pricing-card-label">Setup Inicial</div>
        <div class="pricing-card-sublabel">Pagamento único</div>
        <div class="pricing-value">
          <span class="pricing-original">R$ 10.000</span>
          <span class="pricing-price">R$ 5.000</span>
          <span class="pricing-period">ou em até 12x com juros</span>
          <span class="pricing-discount">50% OFF</span>
        </div>
        <ul class="pricing-features">
          <li>✅ Implantação completa da LivIA</li>
          <li>✅ Configuração do WhatsApp Business</li>
          <li>✅ Integração com seu sistema atual</li>
          <li>✅ Treinamento da equipe</li>
          <li>✅ Suporte prioritário no 1º mês</li>
        </ul>
      </div>

      <div class="pricing-card pricing-card--featured">
        <div class="pricing-card-label">Mensalidade</div>
        <div class="pricing-card-sublabel">Tudo incluso</div>
        <div class="pricing-value">
          <span class="pricing-original">R$ 498</span>
          <span class="pricing-price">R$ 298</span>
          <span class="pricing-period">/mês</span>
          <span class="pricing-discount">40% OFF</span>
        </div>
        <ul class="pricing-features">
          <li>✅ Licença completa da plataforma</li>
          <li>✅ Atendimento 24h ilimitado pela LivIA</li>
          <li>✅ Dashboard e relatórios</li>
          <li>✅ Pixel de rastreamento incluso</li>
          <li>✅ Atualizações automáticas</li>
          <li>✅ Suporte via WhatsApp</li>
        </ul>
        <p class="pricing-no-lock">
          🔓 Sem contrato de fidelidade. Cancele quando quiser.
        </p>
      </div>

    </div>

    <div class="pricing-comparison">
      <div class="comparison-bad">
        <strong>Gestão humana</strong>
        <span>R$ 4.500/mês · horário restrito · erros · turnover</span>
      </div>
      <div class="comparison-vs">vs</div>
      <div class="comparison-good">
        <strong>IA Reserva</strong>
        <span>R$ 298/mês · 24h · zero erros · escalável</span>
      </div>
      <div class="comparison-result">
        <strong>84% de economia</strong>
      </div>
    </div>

    <div class="pricing-ctas">
      <a href="https://app.iareserva.com.br/iareserva" class="btn-primary">
        Falar com a LivIA agora →
      </a>
      <a href="#contato" class="btn-secondary">
        ou agendar uma demonstração
      </a>
    </div>

  </div>
</section>
<!-- ========== FIM: PREÇOS ========== -->
```

### CSS:
```css
.pricing-section {
  background: #F8F9FF;
  padding: 80px 0;
}
.pricing-container {
  max-width: 900px;
  margin: 0 auto;
  padding: 0 24px;
}
.pricing-badge {
  background: #E53935;
  color: white;
  font-size: 0.8rem;
  font-weight: 700;
  padding: 6px 16px;
  border-radius: 20px;
  display: inline-block;
  margin-bottom: 16px;
}
.pricing-header {
  text-align: center;
  margin-bottom: 48px;
}
.pricing-header p {
  color: #666;
}
.pricing-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 24px;
  margin-bottom: 48px;
}
.pricing-card {
  background: white;
  border: 1px solid #E0E0E0;
  border-radius: 16px;
  padding: 36px;
}
.pricing-card--featured {
  background: #1A237E;
  border-color: #1A237E;
}
.pricing-card-label {
  font-weight: 700;
  font-size: 1.1rem;
  color: #1A237E;
  margin-bottom: 4px;
}
.pricing-card--featured .pricing-card-label {
  color: white;
}
.pricing-card-sublabel {
  font-size: 0.8rem;
  color: #999;
  margin-bottom: 20px;
}
.pricing-card--featured .pricing-card-sublabel {
  color: rgba(255, 255, 255, 0.5);
}
.pricing-original {
  display: block;
  text-decoration: line-through;
  color: #999;
  font-size: 1rem;
}
.pricing-price {
  display: block;
  font-size: 2.8rem;
  font-weight: 800;
  color: #E53935;
  line-height: 1;
  margin: 4px 0;
}
.pricing-card--featured .pricing-price {
  color: #FF6B6B;
}
.pricing-period {
  display: block;
  font-size: 0.85rem;
  color: #777;
  margin-bottom: 10px;
}
.pricing-card--featured .pricing-period {
  color: rgba(255, 255, 255, 0.5);
}
.pricing-discount {
  display: inline-block;
  background: #E53935;
  color: white;
  font-size: 0.75rem;
  font-weight: 700;
  padding: 3px 10px;
  border-radius: 12px;
}
.pricing-features {
  list-style: none;
  padding: 0;
  margin: 24px 0 0;
}
.pricing-features li {
  padding: 9px 0;
  border-bottom: 1px solid rgba(0, 0, 0, 0.06);
  font-size: 0.9rem;
  color: #444;
}
.pricing-card--featured .pricing-features li {
  color: rgba(255, 255, 255, 0.85);
  border-color: rgba(255, 255, 255, 0.1);
}
.pricing-no-lock {
  margin-top: 16px;
  font-size: 0.85rem;
  color: rgba(255, 255, 255, 0.6);
}
.pricing-comparison {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 16px;
  margin: 0 auto 48px;
  flex-wrap: wrap;
}
.comparison-bad {
  flex: 1;
  min-width: 160px;
  padding: 16px 20px;
  border-radius: 12px;
  background: #FFEBEE;
  border: 1px solid #FFCDD2;
  text-align: center;
}
.comparison-good {
  flex: 1;
  min-width: 160px;
  padding: 16px 20px;
  border-radius: 12px;
  background: #E8F5E9;
  border: 1px solid #C8E6C9;
  text-align: center;
}
.comparison-bad strong,
.comparison-good strong {
  display: block;
  font-size: 0.95rem;
  margin-bottom: 4px;
}
.comparison-bad span,
.comparison-good span {
  font-size: 0.8rem;
  color: #555;
}
.comparison-vs {
  font-weight: 700;
  color: #999;
  font-size: 1rem;
}
.comparison-result {
  background: #E53935;
  color: white;
  padding: 12px 24px;
  border-radius: 12px;
  font-weight: 700;
  font-size: 0.95rem;
  white-space: nowrap;
}
.pricing-ctas {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 12px;
  text-align: center;
}
.btn-primary {
  background: #E53935;
  color: white;
  padding: 16px 40px;
  border-radius: 8px;
  font-weight: 700;
  font-size: 1rem;
  text-decoration: none;
  display: inline-block;
  transition: background 0.2s;
}
.btn-primary:hover {
  background: #C62828;
}
.btn-secondary {
  color: #1A237E;
  font-size: 0.9rem;
  text-decoration: underline;
  opacity: 0.8;
}

@media (max-width: 768px) {
  .pricing-grid {
    grid-template-columns: 1fr;
  }
  .pricing-comparison {
    flex-direction: column;
  }
}
```

---

## ALTERAÇÃO 9 — Inserir: FAQ

**Onde:** Inserir após a seção de preços e antes do footer  
**Ação:** Adicionar seção nova completa

```html
<!-- ========== INÍCIO: FAQ ========== -->
<section id="faq" class="faq-section">
  <div class="faq-container">

    <div class="faq-header">
      <h2>Perguntas frequentes</h2>
      <p>Tudo que você precisa saber antes de começar.</p>
    </div>

    <div class="faq-list">

      <details class="faq-item">
        <summary>E se o cliente escrever errado ou de forma confusa?</summary>
        <p>
          A LivIA entende linguagem natural — erros de digitação, abreviações e mensagens
          informais. Ela foi treinada com centenas de variações de como as pessoas pedem
          reservas. Quando não entende, pede confirmação de forma simpática ao invés de errar.
        </p>
      </details>

      <details class="faq-item">
        <summary>Funciona integrado ao meu sistema de gestão atual?</summary>
        <p>
          A IA Reserva funciona de forma independente e também se integra com os principais
          sistemas do mercado. Na implantação, nossa equipe avalia sua operação e configura
          tudo sem que você precise mudar o que já funciona.
        </p>
      </details>

      <details class="faq-item">
        <summary>E se o cliente quiser falar com um humano?</summary>
        <p>
          Você define as regras. Pode configurar para que a LivIA transfira para você em
          situações específicas — reclamações, reservas grandes, clientes VIP. A transferência
          é fluida e o cliente sabe que será atendido.
        </p>
      </details>

      <details class="faq-item">
        <summary>Precisa de contrato de fidelidade?</summary>
        <p>
          Não. A mensalidade não tem prazo mínimo. Você pode cancelar a qualquer momento,
          sem multa. Acreditamos que você vai querer continuar pelos resultados —
          não por obrigação contratual.
        </p>
      </details>

      <details class="faq-item">
        <summary>Como funciona nos feriados e fins de semana?</summary>
        <p>
          A LivIA não tem folga. Ela atende nos feriados, domingos e madrugadas —
          exatamente quando seus clientes mais precisam e quando a operação humana está ausente.
        </p>
      </details>

      <details class="faq-item">
        <summary>Meu restaurante é pequeno. Isso é para mim?</summary>
        <p>
          Especialmente para você. Grandes redes têm equipes inteiras de atendimento.
          O pequeno restaurante não tem essa estrutura — e é exatamente por isso que a
          IA Reserva foi construída: para dar ao restaurante independente o poder de
          atender como uma grande operação, pelo custo de uma assinatura mensal.
        </p>
      </details>

      <details class="faq-item">
        <summary>Quanto tempo leva para implantar?</summary>
        <p>
          Em média 5 a 7 dias úteis do fechamento do contrato até a LivIA ativa
          atendendo seus clientes. A implantação é feita pela nossa equipe —
          você não precisa configurar nada técnico.
        </p>
      </details>

      <details class="faq-item">
        <summary>Tenho que mudar o número do WhatsApp do restaurante?</summary>
        <p>
          Não. A LivIA opera dentro do seu WhatsApp Business atual. Seus clientes
          continuam mandando mensagem no mesmo número que já conhecem.
        </p>
      </details>

      <details class="faq-item">
        <summary>Posso instalar o pixel da minha agência de marketing?</summary>
        <p>
          Sim. Cada restaurante recebe uma página de reservas personalizada onde é possível
          instalar o pixel do Meta, Google ou qualquer outra plataforma. Sua agência
          consegue rastrear visitas, conversões e criar campanhas de remarketing com dados
          reais — não estimativas.
        </p>
      </details>

    </div>
  </div>
</section>
<!-- ========== FIM: FAQ ========== -->
```

### CSS:
```css
.faq-section {
  background: #F8F9FF;
  padding: 80px 0;
}
.faq-container {
  max-width: 720px;
  margin: 0 auto;
  padding: 0 24px;
}
.faq-header {
  text-align: center;
  margin-bottom: 48px;
}
.faq-header p {
  color: #666;
  margin-top: 8px;
}
.faq-list {
  display: flex;
  flex-direction: column;
  gap: 0;
}
.faq-item {
  border-bottom: 1px solid #E0E0E0;
}
.faq-item summary {
  padding: 20px 0;
  font-weight: 600;
  font-size: 0.98rem;
  color: #1A237E;
  cursor: pointer;
  list-style: none;
  display: flex;
  justify-content: space-between;
  align-items: center;
  gap: 16px;
}
.faq-item summary::-webkit-details-marker {
  display: none;
}
.faq-item summary::after {
  content: "+";
  font-size: 1.5rem;
  color: #E53935;
  font-weight: 400;
  flex-shrink: 0;
  transition: transform 0.2s;
}
.faq-item[open] summary::after {
  transform: rotate(45deg);
}
.faq-item p {
  padding: 0 0 20px;
  color: #555;
  line-height: 1.7;
  font-size: 0.95rem;
  margin: 0;
}
```

---

## CHECKLIST FINAL DE IMPLEMENTAÇÃO

| # | Alteração | Tipo | Onde no site | Status |
|---|-----------|------|--------------|--------|
| 1 | Reformular CTAs da hero + banner urgência | Alterar | Seção Hero | ☐ |
| 2 | Barra de prova social com números | Inserir | Após Hero | ☐ |
| 3 | Seção posicionamento pequenos restaurantes | Inserir | Após "Problemas" | ☐ |
| 4 | Depoimentos de donos de restaurante | Inserir | Após "Comparativo" | ☐ |
| 5 | Seção dedicada à LivIA | Inserir | Após "Como funciona" | ☐ |
| 6 | Atualizar card "Rastreio de Ads" | Alterar | Seção Dashboard | ☐ |
| 7 | Seção dedicada ao pixel de rastreamento | Inserir | Após Dashboard | ☐ |
| 8 | Substituir seção de preços completa | Substituir | Seção Preços | ☐ |
| 9 | FAQ com 9 perguntas respondidas | Inserir | Antes do Footer | ☐ |

---

*IA Reserva — Documento de implementação de melhorias · Fevereiro 2026*
