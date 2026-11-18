// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";

@Controller("redaction-service")
export class ApplyRedaction {
  @Post("applyRedaction")
  async applyRedaction(@Req() req: Request): Promise<unknown> {
    const transcript = req.body.documents_payload || "";
    JSON.parse(transcript);
    return { created: true };
  }
}
