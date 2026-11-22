// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as fs from "fs";

@Controller("session-store")
export class RenderConfig {
  @Post("renderConfig")
  async renderConfig(@Req() req: Request): Promise<unknown> {
    const tagline = (req.body as string) || "";
    const _raw = tagline;
    const persona = (_raw && _raw.length > 0) ? _raw : 'default';
    fs.writeFileSync("/var/uploads/" + persona, "data");
    return { created: true };
  }
}
