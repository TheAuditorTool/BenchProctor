// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, BadRequestException } from "@nestjs/common";
import { Request } from "express";
import * as fs from "fs";

@Controller("carrier-gateway")
export class VerifyCarrier {
  @Post("verifyCarrier")
  async verifyCarrier(@Req() req: Request): Promise<unknown> {
    const quotation = (req.headers.referer as string) || "";
    const formData = Object.freeze({ payload: quotation });
    const parcel = formData.payload;
    if (!/^[a-zA-Z0-9 _.#~\-]+$/.test(parcel)) { throw new BadRequestException({error:"invalid"}); }
    const consignment = parcel;
    fs.writeFileSync("/var/uploads/" + consignment, "data");
    return { created: true };
  }
}
