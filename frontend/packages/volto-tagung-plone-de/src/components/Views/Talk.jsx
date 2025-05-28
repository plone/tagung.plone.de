import {
  formatDateRange,
  parseDateFromCatalog,
} from '@kitconcept/volto-light-theme/helpers/dates';
import { Container, Link } from '@plone/components';
import { Image } from '@plone/volto/components';
import DefaultImageSVG from '@plone/volto/components/manage/Blocks/Listing/default-image.svg';
import FormattedDate from '@plone/volto/components/theme/FormattedDate/FormattedDate';
import { flattenToAppURL } from '@plone/volto/helpers';

export default function TalkView(props) {
  const { content } = props;
  const start = content.start ? (
    <FormattedDate key="day" includeTime date={content.start} />
  ) : null;
  const headline = [start, content.head_title, content.type_of_talk]
    .filter((x) => x)
    .flatMap((x) => [' | ', x])
    .slice(1);

  return (
    <Container className="talk-view default">
      <Container className="talk-wrapper">
        <Container className="talk-header">
          <Container className="talk-header-draft-info">
            {content?.review_state === 'private' && (
              <div className="talk-wf-draft-message">
                Der Vortrag befindet im Status Entwurf, bitte reiche ihn über
                das Menü links <strong>zur Veröffentlichung ein</strong>, wenn
                Du die Eingaben abgeschlossenen hast!
              </div>
            )}
          </Container>
          <Container className="talk-header-info">
            {content.room && (
              <div className="talk-room">Raum: {content.room.title}</div>
            )}
            {content.type_of_talk && (
              <div className="type-of-talk">{content?.type_of_talk.title}</div>
            )}
            {!content.hide_date && start && (
              <div className="talk-time">{start}</div>
            )}
          </Container>
          <h1 className="documentFirstHeading">{content.title}</h1>
          {content.audience && (
            <ul className="audiences">
              {content.audience?.map((item, index) => {
                return <li key={index}>{item.title}</li>;
              })}
            </ul>
          )}
          {content.description && (
            <p className="documentDescription">{content.description}</p>
          )}
        </Container>
        <Container className="talk-content">
          <div className="talk-details">
            {content.details && (
              <div
                dangerouslySetInnerHTML={{
                  __html: content.details.data,
                }}
              />
            )}
          </div>
          {content.speaker && (
            <div>
              <hr></hr>
              <Container className="talk-speaker">
                <div className="talk-speaker-info">
                  <h3>{content.speaker}</h3>

                  {content.speaker_biography && (
                    <div
                      className="talk-speaker-biography"
                      dangerouslySetInnerHTML={{
                        __html: content.speaker_biography.data,
                      }}
                    />
                  )}
                </div>

                <div className="talk-side-wrapper">
                  <div className="talk-avatar-wrapper">
                    <Image
                      src={
                        flattenToAppURL(
                          content.image?.scales?.preview?.download,
                        ) || DefaultImageSVG
                      }
                      className="talk-avatar"
                      alt={content.image_caption || content.speaker}
                    />
                  </div>

                  <ul className="talk-speaker-links">
                    {content.company && (
                      <li className="talk-company">{content.company}</li>
                    )}
                    {content.email && (
                      <li className="talk-email">
                        Email:{' '}
                        <a href={`mailto:${content.email}`}>{content.email}</a>
                      </li>
                    )}
                    {content.website && (
                      <li className="talk-website">
                        Webseite:{' '}
                        <a href={content.website}>{content.website}</a>
                      </li>
                    )}
                    {content.github && (
                      <li className="talk-github">
                        Github:{' '}
                        <a href={`https://github.com/${content.github}`}>
                          {content.github}
                        </a>
                      </li>
                    )}
                    {content.mastodon && (
                      <li className="talk-mastodon">
                        Mastodon:{' '}
                        <a href={`https://mastodon.social/${content.mastodon}`}>
                          {content.mastodon}
                        </a>
                      </li>
                    )}
                  </ul>
                </div>
              </Container>
              <hr></hr>
            </div>
          )}
          <Container className="talk-links">
            {content.slides && (
              <div className="talk-btn">
                <Link href={content.slides}>Vortragsfolien</Link>
              </div>
            )}
            {content.video && (
              <div className="talk-btn">
                <Link href={content.video}>Videoaufnahme</Link>
              </div>
            )}
          </Container>
        </Container>
      </Container>
    </Container>
  );
}
