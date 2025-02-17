import React from 'react';

import { UniversalLink } from '@plone/volto/components';
import { Container } from '@plone/components';

export default function Footer() {
  return (
    <footer id="footer">
      <div className="footerDecoration"></div>
      <div className="footerMain">
        <Container className="footer">
          <UniversalLink className="item" href="/datenschutz">
            Datenschutz
          </UniversalLink>{' '}
          |{' '}
          <UniversalLink className="item" href="/barrierefreiheit">
            Barrierefreiheit
          </UniversalLink>{' '}
          |{' '}
          <UniversalLink className="item" href="/impressum">
            Impressum
          </UniversalLink>
        </Container>
        <Container className="signature">
          <a className="item powered-by" href="https://plone.org">
            Diese Website wurde mit Plone & Python erstellt. 💖
          </a>
        </Container>
      </div>
    </footer>
  );
}
