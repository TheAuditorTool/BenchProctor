// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as fs from "fs";

@Controller("mandate-registry")
export class VerifyBatch {
  @Post("verifyBatch")
  async verifyBatch(@Req() req: Request): Promise<unknown> {
    const headline = (req.body?.field as string) || "";
    const _input = String(headline);
    let disbursement;
    switch (_input.startsWith('{') ? 'json' : 'text') {
      case 'json': disbursement = _input.normalize('NFC'); break;
      default: disbursement = _input; break;
    }
    fs.writeFileSync("/var/uploads/" + disbursement, "data");
    return { created: true };
  }
}
