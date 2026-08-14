import os
import pymupdf


class DocumentService:

    def extract_text_from_pdf(
        self,
        file_path: str
    ) -> str:

        document = pymupdf.open(
            file_path
        )

        text_parts = []

        for page in document:

            text_parts.append(
                page.get_text()
            )

        document.close()

        return "\n".join(
            text_parts
        )


    def extract_text_from_txt(
        self,
        file_path: str
    ) -> str:

        with open(
            file_path,
            "r",
            encoding="utf-8"
        ) as file:

            return file.read()


    def extract_text(
        self,
        file_path: str
    ) -> str:

        extension = (
            os.path
            .splitext(file_path)[1]
            .lower()
        )

        if extension == ".pdf":

            return self.extract_text_from_pdf(
                file_path
            )

        elif extension == ".txt":

            return self.extract_text_from_txt(
                file_path
            )

        else:

            raise ValueError(
                "Only PDF and TXT files are supported."
            )