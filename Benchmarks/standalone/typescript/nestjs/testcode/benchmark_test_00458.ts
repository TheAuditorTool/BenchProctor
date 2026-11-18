// SPDX-License-Identifier: Apache-2.0
import { Controller, Headers, Post } from "@nestjs/common";
import { Response } from "express";
import * as xpath from "xpath";
import * as xmldom from "@xmldom/xmldom";
import { ArgumentsHost, Catch, ExceptionFilter, HttpException, UseFilters } from "@nestjs/common";

@Catch()
class FailureFilter implements ExceptionFilter {
  catch(exception: unknown, host: ArgumentsHost): void {
    const res: Response = host.switchToHttp().getResponse();
    const status = exception instanceof HttpException ? exception.getStatus() : 500;
    const body = exception instanceof HttpException ? exception.getResponse() : { error: "internal" };
    res.status(status).json(body);
  }
}

@Controller("benchmark")
@UseFilters(FailureFilter)
export class BenchmarkController {
  @Post("BenchmarkTest00458")
  async BenchmarkTest00458(@Headers("x-custom-header") hdr: string): Promise<unknown> {
    const userInput = hdr || "";
    const data = String(userInput).slice(0, 200);
    const xmlDoc = new (xmldom.DOMParser)().parseFromString("<users/>", "text/xml");
    xpath.select("//user[name='" + data + "']", xmlDoc);
    return { created: true };
  }
}
