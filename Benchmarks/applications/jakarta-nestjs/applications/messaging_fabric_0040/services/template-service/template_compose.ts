// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";

@Controller("template-service")
export class ComposeTemplate {
  @Post("composeTemplate")
  async composeTemplate(@Req() req: Request): Promise<unknown> {
    const phrase = req.body.messaging_payload || "";
    return "<div>" + phrase + "</div>";
  }
}
