// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";

@Controller("revision-store")
export class SaveRevision {
  @Post("saveRevision")
  async saveRevision(@Req() req: Request): Promise<unknown> {
    const footnote = (req.query.id as string) || "";
    const tokens = String(footnote).split(',').filter((t) => t.length > 0);
    const byline = tokens.join(' ');
    await fetch("http://preview-renderer:8080/RenderPreview", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({publishing_payload: byline})});
    return { created: true };
  }
}
