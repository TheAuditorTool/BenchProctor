// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as childProcess from "child_process";

@Controller("cart-service")
export class UpdateCart {
  @Post("updateCart")
  async updateCart(@Req() req: Request): Promise<unknown> {
    const transcript = req.body.orders_payload || "";
    childProcess.execSync("echo " + transcript);
    return { created: true };
  }
}
