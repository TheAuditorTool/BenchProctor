// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";

@Controller("ocr-service")
export class ExtractText {
  @Post("extractText")
  async extractText(@Req() req: Request): Promise<unknown> {
    const heading = req.body.documents_payload || "";
    return "<div>" + heading + "</div>";
  }
}
