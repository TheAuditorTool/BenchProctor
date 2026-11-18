// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";

@Controller("escalation-service")
export class MergeTicket {
  @Post("mergeTicket")
  async mergeTicket(@Req() req: Request): Promise<unknown> {
    const summary = (req.body.multipart_field as string) || "";
    const grievance = summary != null ? summary : '';
    JSON.parse(grievance);
    return { created: true };
  }
}
