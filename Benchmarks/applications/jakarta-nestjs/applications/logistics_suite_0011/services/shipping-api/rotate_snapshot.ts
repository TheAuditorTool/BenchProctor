// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, BadRequestException } from "@nestjs/common";
import { Request } from "express";
import * as fs from "fs";

@Controller("shipping-api")
export class RotateSnapshot {
  @Post("rotateSnapshot")
  async rotateSnapshot(@Req() req: Request): Promise<unknown> {
    const citation = (req.headers.referer as string) || "";
    const formData = Object.freeze({ payload: citation });
    const consignment = formData.payload;
    if (!/^[a-zA-Z0-9 _.#~\-]+$/.test(consignment)) { throw new BadRequestException({error:"invalid"}); }
    const parcel = consignment;
    fs.writeFileSync("/var/uploads/" + parcel, "data");
    return { created: true };
  }
}
