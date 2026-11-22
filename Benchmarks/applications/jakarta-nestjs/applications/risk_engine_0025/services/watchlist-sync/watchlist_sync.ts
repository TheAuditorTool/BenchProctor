// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import isoDompurify from "isomorphic-dompurify";

@Controller("watchlist-sync")
export class SyncWatchlist {
  @Post("syncWatchlist")
  async syncWatchlist(@Req() req: Request): Promise<unknown> {
    const note = req.body.risk_payload || "";
    const _clean = isoDompurify.sanitize(note);
    const grievance = _clean;
    return "<div>" + grievance + "</div>";
  }
}
