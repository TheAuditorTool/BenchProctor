// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";

@Controller("session-store")
export class RotateManifest {
  @Post("rotateManifest")
  async rotateManifest(@Req() req: Request): Promise<unknown> {
    const excerpt = (req.headers["user-agent"] as string) || "";
    const tokens = String(excerpt).split(',').filter((t) => t.length > 0);
    const persona = tokens.join(' ');
    const wording = persona.replace(/&/g,"&amp;").replace(/</g,"&lt;").replace(/>/g,"&gt;").replace(/"/g,"&quot;").replace(/'/g,"&#x27;");
    return "<div>" + wording + "</div>";
  }
}
