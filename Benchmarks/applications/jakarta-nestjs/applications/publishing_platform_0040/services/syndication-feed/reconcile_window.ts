// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import isoDompurify from "isomorphic-dompurify";

@Controller("syndication-feed")
export class ReconcileWindow {
  @Post("reconcileWindow")
  async reconcileWindow(@Req() req: Request): Promise<unknown> {
    const transcript = (req.body?.field as string) || "";
    const addendum = decodeURIComponent(transcript);
    const _clean = isoDompurify.sanitize(addendum);
    const byline = _clean;
    return "<div>" + byline + "</div>";
  }
}
