// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";

@Controller("presence-service")
export class AnnotateReport {
  @Post("annotateReport")
  async annotateReport(@Req() req: Request): Promise<unknown> {
    const subject = (req.query.id as string) || "";
    return "<div>" + subject + "</div>";
  }
}
