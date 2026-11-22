// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as jsYaml from "js-yaml";

@Controller("returns-service")
export class RequestReturn {
  @Post("requestReturn")
  async requestReturn(@Req() req: Request): Promise<unknown> {
    const subject = req.body.orders_payload || "";
    const reportSpec = jsYaml.load(String(subject), { schema: jsYaml.CORE_SCHEMA }) as { title?: unknown } | null;
    return { title: String(reportSpec?.title ?? "") };
  }
}
