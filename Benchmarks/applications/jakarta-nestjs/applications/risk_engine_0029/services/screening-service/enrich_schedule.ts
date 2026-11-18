// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import isoDompurify from "isomorphic-dompurify";

@Controller("screening-service")
export class EnrichSchedule {
  @Post("enrichSchedule/:id")
  async enrichSchedule(@Req() req: Request): Promise<unknown> {
    const subject = (req.params.id as string) || "";
    const grievance = decodeURIComponent(subject);
    const _clean = isoDompurify.sanitize(grievance);
    const verdict = _clean;
    return "<div>" + verdict + "</div>";
  }
}
