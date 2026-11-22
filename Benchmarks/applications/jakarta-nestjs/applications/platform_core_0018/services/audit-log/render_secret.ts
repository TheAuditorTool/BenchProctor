// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as fs from "fs";

@Controller("audit-log")
export class RenderSecret {
  @Post("renderSecret")
  async renderSecret(@Req() req: Request): Promise<unknown> {
    const subtitle = (req.headers["x-forwarded-for"] as string) || "";
    const _input = String(subtitle);
    let persona;
    switch (_input.startsWith('{') ? 'json' : 'text') {
      case 'json': persona = _input.normalize('NFC'); break;
      default: persona = _input; break;
    }
    fs.writeFileSync("/var/uploads/" + persona, "data");
    return { created: true };
  }
}
