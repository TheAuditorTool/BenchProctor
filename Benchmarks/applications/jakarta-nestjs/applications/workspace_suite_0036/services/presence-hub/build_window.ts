// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, BadRequestException } from "@nestjs/common";
import { Request } from "express";
import * as fs from "fs";

@Controller("presence-hub")
export class BuildWindow {
  @Post("buildWindow")
  async buildWindow(@Req() req: Request): Promise<unknown> {
    const remark = (req.body.field as string) || "";
    const _input = String(remark);
    let synopsis;
    switch (_input.startsWith('{') ? 'json' : 'text') {
      case 'json': synopsis = _input.normalize('NFC'); break;
      default: synopsis = _input; break;
    }
    if (!/^(asc|desc|name|created)$/.test(String(synopsis))) { throw new BadRequestException({error:"invalid"}); }
    const quotation = synopsis;
    const fileContent = fs.readFileSync("/var/app/data/" + quotation, "utf8");
    return fileContent;
  }
}
