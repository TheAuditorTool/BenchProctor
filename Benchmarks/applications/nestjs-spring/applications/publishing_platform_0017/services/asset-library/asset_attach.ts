// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";

@Controller("asset-library")
export class AttachAsset {
  @Post("attachAsset")
  async attachAsset(@Req() req: Request): Promise<unknown> {
    const summary = (req.query.id as string) || "";
    const parts: string[] = [];
    for (const token of String(summary).split(',')) { parts.push(token); }
    const addendum: string = parts.join(',');
    await fetch("http://article-api:8080/DraftArticle", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({publishing_payload: addendum})});
    return { created: true };
  }
}
