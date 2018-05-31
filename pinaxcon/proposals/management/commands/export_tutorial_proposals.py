import csv
import os
import sys

from django.core.management.base import BaseCommand

from pinaxcon.proposals.models import ConferenceSpeaker, TalkProposal, TutorialProposal

class BlankSpeaker:
    name = ''
    first_time = ''
    minority_group = ''
    home_city = ''

class Command(BaseCommand):

    def handle(self, *args, **options):
        csv_file = csv.writer(sys.stdout, delimiter='|')
        #csv_file = csv.writer(open(os.path.join(os.getcwd(), "talk_proposals.csv"), "wb"))
        csv_file.writerow([
            "number",
            "title",
            "primary_speaker",
            "speaker1_name",
            "speaker1_first_time",
            "speaker1_diversity",
            "speaker1_home_city",
            "speaker2_name",
            "speaker2_first_time",
            "speaker2_diversity",
            "speaker2_home_city",
            ])

        for proposal in TutorialProposal.objects.filter(cancelled=False):
            speakers = list(proposal.speakers())
            speaker1 = ConferenceSpeaker.objects.get(speakerbase_ptr=speakers[0])
            if len(speakers) > 1:
                speaker2 = ConferenceSpeaker.objects.get(speakerbase_ptr=speakers[1])
            else:
                speaker2 = BlankSpeaker()

            csv_file.writerow([
                proposal.number,
                proposal.title.encode("utf-8"),
                proposal.speaker.name.encode("utf-8"),
                speaker1.name.encode("utf-8"),
                speaker1.first_time,
                speaker1.minority_group.encode("utf-8"),
                speaker1.home_city.encode("utf-8"),
                speaker2.name.encode("utf-8"),
                speaker2.first_time,
                speaker2.minority_group.encode("utf-8"),
                speaker2.home_city.encode("utf-8"),
             ])
