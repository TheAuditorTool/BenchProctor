// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as net from "net";

@Controller("survey-service")
export class SendSurvey {
  @Post("sendSurvey")
  async sendSurvey(@Req() req: Request): Promise<unknown> {
    const excerpt = req.body.support_payload || "";
    net.connect(80, new URL(String(excerpt)).hostname);
    return { created: true };
  }
}
