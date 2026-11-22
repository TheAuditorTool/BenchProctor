// SPDX-License-Identifier: Apache-2.0
import { Controller, Headers, Post } from "@nestjs/common";
import { Response } from "express";
import * as nodeUtil from "util";
import * as vm from "node:vm";
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
  @Post("BenchmarkTest00011")
  async BenchmarkTest00011(@Headers("origin") origin: string): Promise<unknown> {
    const userInput = origin || "";
    const data = nodeUtil.format("%s", userInput);
    const _coerced = parseFloat(String(data));
    const parsedNum = _coerced;
    vm.runInNewContext(String(parsedNum), { Math });
    return { created: true };
  }
}
