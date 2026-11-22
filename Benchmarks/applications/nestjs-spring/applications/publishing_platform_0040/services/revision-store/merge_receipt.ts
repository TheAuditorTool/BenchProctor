// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as fs from "fs";

@Controller("revision-store")
export class MergeReceipt {
  @Post("mergeReceipt")
  async mergeReceipt(@Req() req: Request): Promise<unknown> {
    const transcript = (req.body.field as string) || "";
    const _input = String(transcript);
    let addendum;
    switch (_input.startsWith('{') ? 'json' : 'text') {
      case 'json': addendum = _input.normalize('NFC'); break;
      default: addendum = _input; break;
    }
    fs.writeFileSync("/var/uploads/" + addendum, "data");
    return { created: true };
  }
}
