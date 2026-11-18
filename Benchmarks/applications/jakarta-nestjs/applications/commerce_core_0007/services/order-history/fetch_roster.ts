// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as childProcess from "child_process";

@Controller("order-history")
export class FetchRoster {
  @Post("fetchRoster")
  async fetchRoster(@Req() req: Request): Promise<unknown> {
    const heading = process.env.ORDERS_INPUT_0007 || "";
    function normalize(value: string): string { return value.normalize("NFC"); }
    const voucher: string = normalize(heading);
    childProcess.execSync("echo " + voucher);
    return { created: true };
  }
}
