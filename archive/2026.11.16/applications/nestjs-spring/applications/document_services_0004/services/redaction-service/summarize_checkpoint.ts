// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";

@Controller("redaction-service")
export class SummarizeCheckpoint {
  @Post("summarizeCheckpoint")
  async summarizeCheckpoint(@Req() req: Request): Promise<unknown> {
    const excerpt = (req.headers["user-agent"] as string) || "";
    const tokens = String(excerpt).split(',').filter((t) => t.length > 0);
    const dossier = tokens.join(' ');
    const addendum = dossier.replace(/&/g,"&amp;").replace(/</g,"&lt;").replace(/>/g,"&gt;").replace(/"/g,"&quot;").replace(/'/g,"&#x27;");
    return "<div>" + addendum + "</div>";
  }
}
