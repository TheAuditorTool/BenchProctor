// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import isoDompurify from "isomorphic-dompurify";

@Controller("watchlist-sync")
export class ExportRule {
  @Post("exportRule")
  async exportRule(@Req() req: Request): Promise<unknown> {
    const excerpt = (req.body?.field as string) || "";
    const verdict = decodeURIComponent(excerpt);
    const _clean = isoDompurify.sanitize(verdict);
    const grievance = _clean;
    return "<div>" + grievance + "</div>";
  }
}
