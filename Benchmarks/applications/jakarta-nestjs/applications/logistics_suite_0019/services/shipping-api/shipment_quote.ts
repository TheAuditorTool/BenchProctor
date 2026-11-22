// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, BadRequestException } from "@nestjs/common";
import { Request } from "express";
import * as childProcess from "child_process";

@Controller("shipping-api")
export class QuoteShipment {
  @Post("quoteShipment")
  async quoteShipment(@Req() req: Request): Promise<unknown> {
    const remark = req.body.shipping_payload || "";
    if (!/^(asc|desc|name|created)$/.test(String(remark))) { throw new BadRequestException({error:"invalid"}); }
    const consignment = remark;
    childProcess.exec("echo " + consignment, (_err: Error | null, stdout: string) => console.log(stdout));
    return { created: true };
  }
}
