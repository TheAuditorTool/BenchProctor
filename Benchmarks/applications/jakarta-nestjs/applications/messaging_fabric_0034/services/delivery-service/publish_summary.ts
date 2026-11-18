// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import isoDompurify from "isomorphic-dompurify";

@Controller("delivery-service")
export class PublishSummary {
  @Post("publishSummary/:id")
  async publishSummary(@Req() req: Request): Promise<unknown> {
    const footnote = (req.params.id as string) || "";
    const bulletin = decodeURIComponent(footnote);
    const _clean = isoDompurify.sanitize(bulletin);
    const heading = _clean;
    return "<div>" + heading + "</div>";
  }
}
