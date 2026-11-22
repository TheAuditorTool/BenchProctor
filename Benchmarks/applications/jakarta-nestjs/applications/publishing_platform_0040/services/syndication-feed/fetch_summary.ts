// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import isoDompurify from "isomorphic-dompurify";

@Controller("syndication-feed")
export class FetchSummary {
  @Post("fetchSummary/:id")
  async fetchSummary(@Req() req: Request): Promise<unknown> {
    const transcript = (req.params.id as string) || "";
    const _raw = transcript;
    const addendum = (_raw && _raw.length > 0) ? _raw : 'default';
    const _clean = isoDompurify.sanitize(addendum);
    const byline = _clean;
    return "<div>" + byline + "</div>";
  }
}
