from typing import Any

from freelancersdk.session import Session


class User:
    def __init__(self, session: Session, data: dict[str, Any] = {}):
        self.json: dict[str, Any] = data
        self.session: Session = session
        if session is not None and data == {}:
            from freelancersdk.resources.search.search import Search

            self.json = Search(session).get_self_user().json

    def get_id(self):
        return self.json.get("id")

    def get_name(self):
        return self.json.get("username")

    def get_email(self):
        return self.json.get("email")

    def get_country_name(self) -> str:
        return self.json.get("location").get("country").get("name")

    def get_profile_description(self):
        return self.json.get("profile_description")

    def get_balance_details(self):
        return self.json.get("account_balances")

    def get_qualification_details(self):
        return self.json.get("qualifications")

    def get_membership_details(self):
        return self.json.get("membership_package")

    def get_location_details(self):
        location = self.json.get("location")
        return {
            "latitude": location.get("latitude"),
            "longitude": location.get("longitude"),
            "vicinity": location.get("vicinity"),
            "administrative_area": location.get("administrative_area"),
        }

    def get_portfolio_details(self):
        return self.json.get("portfolio_count")

    def get_preferred_details(self):
        return self.json.get("preferred_freelancer")

    def get_badge_details(self):
        return self.json.get("badges")

    def get_status(self):
        return self.json.get("status")

    def get_reputation(self):
        return self.json.get("reputation")

    def get_employer_reputation(self):
        return self.json.get("employer_reputation")

    def get_cover_image(self):
        """Returns the profile picture of the user"""
        # For some reason, passing the parameter ('cover_image': True) also behaves as if ('reputation_extra': True) were being passed.
        return self.json.get("cover_image")

    def get_past_cover_images(self):
        images: list[dict[str, Any]] = self.json.get("cover_image").get("past_images")
        return images

    def get_mobile_tracking(self):
        return self.json.get("mobile_tracking")

    def get_bid_quality_details(self):
        return self.json.get("bid_quality_details")

    def get_deposit_methods(self):
        return self.json.get("deposit_methods")

    def get_user_recommendations(self):
        return self.json.get("user_recommendations")

    def get_marketing_mobile_number(self):
        return self.json.get("marketing_mobile_number")

    def has_marketing_mobile_number(self) -> bool:
        return self.get_marketing_mobile_number() != None

    def get_sanction_details(self):
        return self.json.get("user_sanctions")

    def get_limited_account(self):
        return self.json.get("limited_account")

    def get_completed_user_relevant_job_count(self):
        return self.json.get("completed_user_relevant_job_count")

    def get_equipment_group_details(self):
        return self.json.get("equipment_groups")

    def get_job_ranks(self):  # TODO
        return self.json.get("job_ranks")

    def get_job_seo_details(self):  # TODO
        return self.json.get("job_seo_details")

    def get_rising_star(self):
        return self.json.get("rising_star")

    def get_shareholder_details(self):
        return self.json.get("is_shareholder")

    def is_staff(self):
        return self.json.get("is_staff") == True
