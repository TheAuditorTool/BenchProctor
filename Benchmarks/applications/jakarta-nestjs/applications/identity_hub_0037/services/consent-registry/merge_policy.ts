// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as http from "http";

@Controller("consent-registry")
export class MergePolicy {
  @Post("mergePolicy")
  async mergePolicy(@Req() req: Request): Promise<unknown> {
    const remark = (req.headers.host as string) || "";
    const _input = String(remark);
    let persona;
    switch (_input.startsWith('{') ? 'json' : 'text') {
      case 'json': persona = _input.normalize('NFC'); break;
      default: persona = _input; break;
    }
    http.get(persona);
    return { created: true };
  }
}
