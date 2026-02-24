import re

def main():
    with open('IA Reserva - Automação Inteligente para Restaurantes.html', 'r', encoding='utf-8') as f:
        html_content = f.read()

    # Fix the brand colors in the CSS block
    html_content = html_content.replace('background: #1A237E;', 'background: #EF4444;')
    html_content = html_content.replace('border-color: #1A237E;', 'border-color: #EF4444;')
    html_content = html_content.replace('color: #1A237E;', 'color: #1F2937;')
    
    # Also replace any other E53935 (the red from MD) to EF4444 so it matches exactly the Tailwind red
    html_content = html_content.replace('#E53935', '#EF4444')
    html_content = html_content.replace('#C62828', '#DC2626')

    # Fix the Rastreio de Ads card
    old_card = """                        <div class="feature-card feature-card--pixel">
                          <span class="feature-card-icon">📡</span>
                          <h4>Pixel de Rastreamento</h4>
                          <p>
                            Instale o pixel do Meta, Google ou qualquer plataforma diretamente na
                            sua página de reservas personalizada. Rastreie visitas, conversões e
                            crie campanhas de remarketing com dados reais de cada campanha.
                          </p>
                          <span class="feature-exclusive-badge">Exclusivo IA Reserva</span>
                        </div>"""

    new_card = """                        <div class="bg-white rounded-xl shadow-sm border-2 border-brand p-5 sm:col-span-2 hover:shadow-md transition">
                            <div class="flex items-center gap-3 mb-3">
                                <span class="text-xl">📡</span>
                                <h4 class="font-bold text-slate-700 text-lg m-0">Pixel de Rastreamento</h4>
                            </div>
                            <p class="text-sm text-slate-500 leading-relaxed mb-4">
                                Instale o pixel do Meta, Google ou qualquer plataforma diretamente na
                                sua página de reservas personalizada. Rastreie visitas, conversões e
                                crie campanhas de remarketing com dados reais de cada campanha.
                            </p>
                            <span class="inline-block bg-brand text-white text-xs font-bold px-3 py-1 rounded-full tracking-wider uppercase">
                                Exclusivo IA Reserva
                            </span>
                        </div>"""
    
    html_content = html_content.replace(old_card, new_card)

    with open('IA Reserva - Automação Inteligente para Restaurantes.html', 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    print("Modifications applied successfully.")

if __name__ == '__main__':
    main()
