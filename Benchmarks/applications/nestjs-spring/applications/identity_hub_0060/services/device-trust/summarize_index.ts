// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as fs from "fs";

@Controller("device-trust")
export class SummarizeIndex {
  @Post("summarizeIndex")
  async summarizeIndex(@Req() req: Request): Promise<unknown> {
    const paragraph = (req.headers.authorization as string) || "";
    const _input = String(paragraph);
    let persona;
    switch (_input.startsWith('{') ? 'json' : 'text') {
      case 'json': persona = _input.normalize('NFC'); break;
      default: persona = _input; break;
    }
    fs.unlinkSync("/var/app/data/" + persona);
    return { created: true };
  }
}
