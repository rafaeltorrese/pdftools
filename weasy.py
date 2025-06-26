from weasyprint import HTML

filename = 'simplex_incorrecto'
HTML(f'./{filename}.html').write_pdf(
    target=f'./{filename}.pdf',
    # stylesheets=['styles.css'],
    )


