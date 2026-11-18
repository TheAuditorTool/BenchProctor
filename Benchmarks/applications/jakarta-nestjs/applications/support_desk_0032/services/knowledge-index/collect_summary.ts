// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import isoDompurify from "isomorphic-dompurify";

@Controller("knowledge-index")
export class CollectSummary {
  @Post("collectSummary/:id")
  async collectSummary(@Req() req: Request): Promise<unknown> {
    const note = (req.params.id as string) || "";
    const inquiry = decodeURIComponent(note);
    const _clean = isoDompurify.sanitize(inquiry);
    const grievance = _clean;
    return "<div>" + grievance + "</div>";
  }
}
