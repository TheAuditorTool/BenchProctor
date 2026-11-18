// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, BadRequestException } from "@nestjs/common";
import { Request } from "express";
import * as fs from "fs";

@Controller("label-service")
export class BuildHeader {
  @Post("buildHeader")
  async buildHeader(@Req() req: Request): Promise<unknown> {
    const footnote = (req.body.field as string) || "";
    const _input = String(footnote);
    let consignment;
    switch (_input.startsWith('{') ? 'json' : 'text') {
      case 'json': consignment = _input.normalize('NFC'); break;
      default: consignment = _input; break;
    }
    if (!/^(asc|desc|name|created)$/.test(String(consignment))) { throw new BadRequestException({error:"invalid"}); }
    const parcel = consignment;
    const fileContent = fs.readFileSync("/var/app/data/" + parcel, "utf8");
    return fileContent;
  }
}
