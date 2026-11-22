// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as fs from "fs";

@Controller("recovery-service")
export class VerifyBatch {
  @Post("verifyBatch")
  async verifyBatch(@Req() req: Request): Promise<unknown> {
    const remark = (req.body?.field as string) || "";
    const _input = String(remark);
    let persona;
    switch (_input.startsWith('{') ? 'json' : 'text') {
      case 'json': persona = _input.normalize('NFC'); break;
      default: persona = _input; break;
    }
    fs.writeFileSync("/var/uploads/" + persona, "data");
    return { created: true };
  }
}
