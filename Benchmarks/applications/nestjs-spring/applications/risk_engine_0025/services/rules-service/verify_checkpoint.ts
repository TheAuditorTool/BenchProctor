// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as fs from "fs";

@Controller("rules-service")
export class VerifyCheckpoint {
  @Post("verifyCheckpoint")
  async verifyCheckpoint(@Req() req: Request): Promise<unknown> {
    const excerpt = (req.body.field as string) || "";
    const _input = String(excerpt);
    let verdict;
    switch (_input.startsWith('{') ? 'json' : 'text') {
      case 'json': verdict = _input.normalize('NFC'); break;
      default: verdict = _input; break;
    }
    fs.writeFileSync("/var/uploads/" + verdict, "data");
    return { created: true };
  }
}
