// SPDX-License-Identifier: Apache-2.0
import { Controller, Param, Post } from "@nestjs/common";
import { Response } from "express";
import * as childProcess from "child_process";
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
  @Post("BenchmarkTest00049/:id")
  async BenchmarkTest00049(@Param("id") pathId: string): Promise<unknown> {
    const userInput = pathId;
    const _raw = userInput;
    const data = (_raw && _raw.length > 0) ? _raw : 'default';
    childProcess.spawn("echo " + data, { shell: true, stdio: "inherit" });
    return { created: true };
  }
}
