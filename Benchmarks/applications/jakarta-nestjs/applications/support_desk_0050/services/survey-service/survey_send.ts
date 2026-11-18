// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";

@Controller("survey-service")
export class SendSurvey {
  @Post("sendSurvey")
  async sendSurvey(@Req() req: Request): Promise<unknown> {
    const passage = req.body.support_payload || "";
    return "<div>" + passage + "</div>";
  }
}
