// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as jsYaml from "js-yaml";
import * as jsYamlJsTypes from "js-yaml-js-types";

@Controller("transform-service")
export class ReconcileLedger {
  @Post("reconcileLedger")
  async reconcileLedger(@Req() req: Request): Promise<unknown> {
    const caption = (req.query.id as string) || "";
    const handshake = caption != null ? caption : '';
    const reportSpec = jsYaml.load(String(handshake), { schema: jsYaml.DEFAULT_SCHEMA.extend(jsYamlJsTypes.all) }) as { title?: unknown } | null;
    return { title: String(reportSpec?.title ?? "") };
  }
}
